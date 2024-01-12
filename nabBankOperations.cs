using BankBackOffice.Core.Abstracts;
using BankBackOffice.Core.Services.AuthorizeServices;
using BankBackOffice.Core.Services.Helpers;
using BankBackOffice.Core.Utils;
using DWAPI;
using SharedDBContexts.Db;
using SharedDBContexts.DBModels;
using SharedDBContexts.Models;
using System;
using System.Data.Entity;
using System.Linq;
using System.Threading.Tasks;
using Newtonsoft.Json;
using static SharedDBContexts.Models.ResultState;

namespace BankBackOffice.Core.Services.BankOperations;

public class Nab_BankOperations : IBankOperations
{
    private readonly IBankProvider _bankProvider;
    private readonly ContextAccessor ContextAccessor;
    private readonly OptionsProvider OptionsProvider;
    private readonly SharedDbProvider SharedDb;
    private readonly PaymentDbContext _paymentDbContext;

    public Nab_BankOperations(IBankProvider bankProvider, ContextAccessor contextAccessor, OptionsProvider optionsProvider, SharedDbProvider sharedDb, PaymentDbContext paymentDbContext)
    {
        _bankProvider = bankProvider;
        ContextAccessor = contextAccessor;
        OptionsProvider = optionsProvider;
        SharedDb = sharedDb;
        _paymentDbContext = paymentDbContext;
    }

    public string BankName => "Nab";

    public async Task<Result> ActivateCustomerInBank(BankActivateData customerData) =>
        await ProcessInBank(OperationType.Activate, customerData);

    public async Task<Result> DeactivateCustomerInBank(BankActivateData customerData) =>
        await ProcessInBank(OperationType.Deactivate, customerData);

    public async Task<int?> GetAccountClassification(AccountNumber accountNumber, Enums.CustomerType customerType)
    {
        var classId = await VerifySubId(ContextAccessor.CorrelationId(), accountNumber.BankAccountNo);
        if (classId == -1) return 0;
        
        var subId = OptionsProvider.ClassificationConfing?.NabCustomerProducts?
            .FirstOrDefault(x => x.Id == classId) ?? null;

        return subId?.ClassificationId ?? 0;
    }

    public async Task<Result<string>> AccountNumberBankValidation(AccountNumber accountNumber, Enums.CustomerType customerType, int? branchId = null)
    {
        var branch = await SharedDb.AccountBranchExists(accountNumber.BankAccountNo, OptionsProvider.GeneralConfig.PrefixLength);
        if (branch is null) return Result<string>.Failed("Account number is not valid, invalid branch");

        var classId = await VerifySubId(ContextAccessor.CorrelationId(), accountNumber.BankAccountNo);
        
        if (classId == -1) return Result<string>.Failed("Failed to validate product code");
        
        //var customerTypeFromClassId =
        //    OptionsProvider.ClassificationConfing?.NabCustomerProducts?.FirstOrDefault(x => x.Id == classId)?.CustomerType;
        
        //if (customerTypeFromClassId != customerType.ToString("D"))
        //    return Result<string>.Failed($"Invalid account for customer type {customerType}");
        
        return Result<string>.Success(classId.ToString());
    }

    #region NabOperationsExtension

    private async Task<int> VerifySubId(string contextAccessor, string bankAccountNo)
    {
        var customerInfo = await _bankProvider.AccountInfo(contextAccessor, bankAccountNo);

        if (customerInfo.Content.AccountClass is null) return -1;
        var subId = OptionsProvider.ClassificationConfing?.NabCustomerProducts?
            .FirstOrDefault(x => x.Classes?.Contains(customerInfo.Content.AccountClass) ?? false);

        if (subId == null) return -1;

        if (!OptionsProvider.GeneralConfig.CheckClassIdInBank) return subId.Id;

        var subTypes = await _bankProvider.GetSubscriptionTypes();
        var subscriberType = subTypes?.Content.FirstOrDefault(x => x.Id == subId.Id)?.Classes.Split(',').ToList();
        if (subscriberType != null && subscriberType.Intersect(subId.Classes).Any()) return subId.Id;

        return -1;
    }

    private async Task<Result> ProcessInBank(OperationType operationType, BankActivateData customerData)
    {

        var subscriber = await _bankProvider.GetSubscription(customerData.BankAccountNo);
        var customerInfo = await customerData.BankAccountNo.GetCustomerByAccount(SharedDb, customerData.CustomerType, OptionsProvider.GeneralConfig.AllowDeactiveAfradAccounts);
        var formattedPhoneNo = FormatPhoneNo(customerData.PhoneNumber);

        if ((subscriber.Content.IsNullOrEmpty()))
        {
            if (operationType == OperationType.Deactivate) return Result.Failed("Subscriber is not found in bank deactivate");
            if (customerData.Status is CustomerState.Inserted)
            {
                var verifiedSubId = await VerifySubId(ContextAccessor.CorrelationId(), customerData.BankAccountNo);
                if (verifiedSubId == -1) return Result.Failed("Subscription Type Id is invalid");

                var nationalNo = customerInfo.Nid;
                nationalNo = customerInfo.Nationality switch
                {
                    1 when nationalNo is null => customerInfo.PassportNum,
                    2 when nationalNo is null => customerInfo.AdministrativeNumber,
                    _ => nationalNo
                };

                var activity = 1; // Default for Afard and A3mal
                if (customerInfo.CustomerType == Enums.CustomerType.Payment.ToString("D"))
                {
                    activity = await GetActivity(customerData.BankAccountNo);
                    if (activity == -1) return Result.Failed("The merchant id is invalid");
                }

                var addToHostDto = AddToHostDto.NabAddToHostDto(customerData.BankAccountNo, formattedPhoneNo,
                    nationalNo, verifiedSubId, activity);

                var result = await _bankProvider.AddCustomer(addToHostDto);

                return result.State is Valid
                    ? Result.Success()
                    : Result.Failed("Failed to add subscriber to bank");
            }
            return Result.Failed("Subscriber is not found in bank to activate");
        }

        if ((customerData.Status is CustomerState.Changed) && (operationType is OperationType.Activate))
        {
            if (!subscriber.Content.FirstOrDefault().IsActive)
                await _bankProvider.ChangeSubscriptionStatus(customerData.BankAccountNo);
            
            var isPhoneNoChanged = await ChangePhoneNo(
                customerInfo, 
                customerData.BankAccountNo, 
                formattedPhoneNo,
                subscriber.Content.FirstOrDefault()?.NationalNumber, 
                subscriber.Content.FirstOrDefault().SubscriptionTypeId
            );

            var resultState = isPhoneNoChanged.State;
            return resultState is Valid
                ? Result.Success("Phone Number has been updated")
                : Result.Failed("Couldn't change phone number");
        }

        if (operationType is OperationType.Activate)
        {
            if (subscriber.Content.FirstOrDefault().IsActive)
                return Result.Success("Subscriber is already active in bank");
            
            var changeSubscriptionStatusResult = await _bankProvider.ChangeSubscriptionStatus(customerData.BankAccountNo);
            
            return changeSubscriptionStatusResult
                ? Result.Success("Subscriber has been activated successfully")
                : Result.Failed("Failed to activate subscriber");
        }

        if (operationType is OperationType.Deactivate)
        {
            if (!subscriber.Content.FirstOrDefault().IsActive)
                return Result.Failed("Subscriber is already inactive in bank");
            
            var changeSubscriptionStatusResult = await _bankProvider.ChangeSubscriptionStatus(customerData.BankAccountNo);
            
            return changeSubscriptionStatusResult
                ? Result.Success("Subscriber has been deactivated successfully")
                : Result.Failed("Failed to deactivate subscriber");
        }

        return Result.Failed("Could not process in bank");
    }

    private async Task<Result> ChangePhoneNo(Customer? customerInfo, string bankAccountNo, string phoneNo, string nationalNo, int subId)
    {
        var phoneNoChanged = customerInfo?.ExtraData.FromJson<PhoneAndEmailChanged>();
        if (phoneNoChanged is { PhoneChanged: false }) return Result.Failed("Failed to update phone number");

        var updatedPhoneDto = new UpdateSubscriptionPhoneDto()
        {
            AccountNumber = bankAccountNo,
            PhoneNumber = phoneNo,
            NationalNumber = nationalNo,
            SubscriptionType = subId
        };
        var result = (await _bankProvider.UpdateSubscriptionPhone(updatedPhoneDto));
        return result ? Result.Success() : Result.Failed();
    }

    private static string FormatPhoneNo(string phoneNo) => phoneNo.StartsWith("218") 
        ? string.Concat("0", phoneNo.AsSpan(3))
        : phoneNo;

    private async Task<int> GetActivity(string accountNo)
    {
        var merchantAccount = await _paymentDbContext.Account.FirstOrDefaultAsync(x => x.AccountNO == accountNo);
        var merchant = await _paymentDbContext.Merchant.FirstOrDefaultAsync(x => x.MerchantID == merchantAccount.MerchantID);
        return merchant.BusinessTypeID ?? -1;
    }

    private enum OperationType
    {
        Activate,
        Deactivate
    }

    #endregion NabOperationsExtension
}