using AdapterServices.Abstracts;
using AdapterServices.Clients.WAH_V2.Abstracts;
using AdapterServices.Clients.WAH_V2.WahdaHelpers;
using Microsoft.AspNetCore.Routing;
using Microsoft.IdentityModel.Tokens;
using MittDevQA.Utils.Vm;
using OpenTracing;
using Serilog;
using AccountType = AdapterServices.Abstracts.AccountType;

namespace AdapterServices.Mock
{
    public class FakeBankInquiriesAPI : FackBaseBankAPI, IBankInquiriesAPI
    {
        public async Task<OperationResult<List<LiBankCustomerAccounts>>> GetCustomerAccounts(string correlationId, string customerCode)
        {
            if (customerCode.IsNullOrEmpty() || customerCode.Length != 7)
                return OperationResult<List<LiBankCustomerAccounts>>.UnValid("customer code must be 7 digits long");
            
            await Task.CompletedTask;
            
            var fakeCustomerAccounts = new List<LiBankCustomerAccounts>
            {
                new()
                {
                    AccNo = $"{customerCode}44111444",
                    AccName = "علي محمد",
                    Opr_state = "999",
                },
                new()
                {
                    AccNo = $"{customerCode}88333888",
                    AccName = "أيوب رقم واحد",
                    Opr_state = "999",
                },
                new()
                {
                    AccNo = $"{customerCode}77111777",
                    AccName = "عبد الله الفقيه",
                    Opr_state = "999",
                },
                                new()
                {
                    AccNo = $"{customerCode}44111444",
                    AccName = "علي محمد",
                    Opr_state = "999",
                },
                new()
                {
                    AccNo = $"{customerCode}88333888",
                    AccName = "أيوب رقم اثنين",
                    Opr_state = "999",
                },
                new()
                {
                    AccNo = $"{customerCode}77111777",
                    AccName = "عبد الله الفقيه",
                    Opr_state = "999",
                },
                                new()
                {
                    AccNo = $"{customerCode}44111444",
                    AccName = "علي محمد",
                    Opr_state = "999",
                },
                new()
                {
                    AccNo = $"{customerCode}88202888",
                    AccName = "أيوب رقم ثلاثة",
                    Opr_state = "999",
                },
                new()
                {
                    AccNo = $"{customerCode}77111777",
                    AccName = "عبد الله الفقيه",
                    Opr_state = "999",
                },
                                new()
                {
                    AccNo = $"{customerCode}44111444",
                    AccName = "علي محمد",
                    Opr_state = "999",
                },
                new()
                {
                    AccNo = $"{customerCode}88333888",
                    AccName = "أيوب رقم أربعة",
                    Opr_state = "999",
                },
                new()
                {
                    AccNo = $"{customerCode}77111777",
                    AccName = "عبد الله الفقيه",
                    Opr_state = "999",
                },
                                new()
                {
                    AccNo = $"{customerCode}44111444",
                    AccName = "علي محمد",
                    Opr_state = "999",
                },
                new()
                {
                    AccNo = $"{customerCode}88333888",
                    AccName = "أيوب رقم خمسة",
                    Opr_state = "999",
                },
                new()
                {
                    AccNo = $"{customerCode}77111777",
                    AccName = "عبد الله الفقيه",
                    Opr_state = "999",
                },
            };
            
            return OperationResult<List<LiBankCustomerAccounts>>.Valid(fakeCustomerAccounts);
        }

        public string BankName => "مصرف تجريبي";

        public string BankCode => "FBank";

        public string BranchSample => "";

        public FakeBankInquiriesAPI(IServiceProvider serviceProvider, ILogger logger, ITracer tracer) : base(serviceProvider, logger, tracer)
        {
        }

        public async Task<string> GetBranchName(string correlationId, string accountNumber,
            AccountType accountType = AccountType.Current, bool withLogging = true)
        {
            using IScope scope = _tracer.BuildSpan("FackBankAPI:GetBranchName").WithTag("TraceId", correlationId)
                .StartActive(finishSpanOnDispose: true);
            try
            {
                await Task.CompletedTask;
                var name = "حي الانلدلس";

                if (withLogging)

                    _semilogger.Log(new { correlationId, accountNumber }, name,
                       $"FackBankAPI" + ("InquiriesAPI  execute GetBranchName on db" +
                        "with account number {@accountNumber} " +
                          " and fetched name {@name}  {@TraceId}", accountNumber, name, correlationId));

                return name;
            }
            catch (Exception ex)
            {
                _semilogger.Log(accountNumber, null,
                   $"FackBankAPI" + ("InquiriesAPI  error happen  when execute GetBranchName on db " +
                                    "with {@accountnumber} {@TraceId}", accountNumber, correlationId), ex);

                return null;
            }
        }

        public Task<string> GetBranchPrefix(string correlationId, string accountNumber, bool withLogging = true)
        {
            return Task.FromResult( accountNumber.Substring(0, 3));
        }

        public async Task<string> GetName(string correlationId, string accountNumber)
        {
            using IScope scope = _tracer.BuildSpan("FackBankAPI:GetName").WithTag("TraceId", correlationId)
                .StartActive(finishSpanOnDispose: true);
            try
            {
                await Task.CompletedTask;
                var name = "اسامة محمد";

                _semilogger.Log(new { accountNumber, name, correlationId }, name,
                      $"FackBank" + ("API  execute GetName(GETNAME in wcf) " +
                      "with account number {@accountNumber} and fetched name {@name} {@TraceId}",
                       accountNumber, name, correlationId));

                return name;
            }
            catch (Exception ex)
            {
                _semilogger.Log(accountNumber, null,
                $"FackBank" + ("API error happen  when execute GetName (GETNAME in wcf)  " +
                   "with {@accountnumber} {@TraceId}", accountNumber, correlationId), ex, traceId: correlationId);

                return null;
            }
        }

        public async Task<OperationResult<string>> GetNamePortal(string correlationId, string accountNumber)
        {
            using IScope scope = _tracer.BuildSpan("FackBankAPI:GetName").WithTag("TraceId", correlationId)
                .StartActive(finishSpanOnDispose: true);
            try
            {
                await Task.CompletedTask;
                var name = "اسامة محمد";

                _semilogger.Log(new { accountNumber, name, correlationId }, name,
                    $"FackBank" + ("API  execute GetNamePortal (GetNamePortal in wcf) " +
                                   "with account number {@accountNumber} and fetched name {@name} {@TraceId}",
                        accountNumber, name, correlationId));

                return OperationResult<string>.Valid(name);
            }
            catch (Exception ex)
            {
                _semilogger.Log(accountNumber, null,
                    $"Fake Bank" + ("API error happen  when execute GetNamePortal (GetNamePortal in wcf)  " +
                                   "with {@accountnumber} {@TraceId}", accountNumber, correlationId), ex, traceId: correlationId);

                return null;
            }
        }

        public async Task<int> GetEmailStatementCount(string correlationId, string accountNumber, DateTime fromDate,
            DateTime toDate)
        {
            using IScope scope = _tracer.BuildSpan("FackBankAPI:GetEmailStatementCount")
                .WithTag("TraceId", correlationId).StartActive(finishSpanOnDispose: true);
            try
            {
                await Task.CompletedTask;
                var countOfStatement = 100;

                _semilogger.Log(new { correlationId, accountNumber, fromDate, toDate }, countOfStatement,
                       $"FakeBank" + (" API  execute GetEmailStatementCount (EmailStatementCount) {@dto}" +
                        "and number of rows is {@countOfStatement} {@TraceId}", new { correlationId, accountNumber, fromDate, toDate }, countOfStatement, correlationId));
                return countOfStatement;
            }
            catch (Exception ex)
            {
                _semilogger.Log(new { correlationId, accountNumber, fromDate, toDate }, null,
                      $"FakeBank" + (" API error happen  when execute GetEmailStatementCount(EmailStatementCount )  " +
                       "with {@dto} {@TraceId}", new { correlationId, accountNumber, fromDate, toDate },
                       correlationId), ex, traceId: correlationId);

                return -1;
            }
        }

        public async Task<EmailStatementDTO> GetEmailStatement(string correlationId, string accountNumber,
            DateTime fromDate, DateTime toDate)
        {
            using IScope scope = _tracer.BuildSpan("FackBankAPI:GetEmailStatement").WithTag("TraceId", correlationId)
                .StartActive(finishSpanOnDispose: true);
            try
            {
                FackUtility.InquieriesNumberOfRetries++;
                await Task.Delay(1000);
                if (FackUtility.CurrentFakeState == FakeState.Success ||
                    FackUtility.CurrentFakeState == FakeState.DuplicatedFromStart ||
                    (FackUtility.CurrentFakeState ==
                      FakeState.BankOffline2Success ||
                      FackUtility.CurrentFakeState == FakeState.Unknown2Success) &&
                     FackUtility.InquieriesNumberOfRetries >= 3)
                {
                    var fackStatment = generateFackDTO();
                    _semilogger.Log(new { correlationId, accountNumber, fromDate, toDate }, fackStatment,
                      $"FakeBank" + ("API  execute GetEmailStatement {@dto} and fetched {@rowsCount} row {@TraceId}",
                      new { correlationId, accountNumber, fromDate, toDate }, fackStatment.BankStatement.Count + 1, correlationId));

                    return fackStatment;
                }
                else
                {
                    throw new Exception("there's exception happen with GetEmailStatment");
                }
            }
            catch (Exception ex)
            {
                _semilogger.Log(new { correlationId, accountNumber, fromDate, toDate }, null,
              $"{BankCode}" + ("API error happen  when execute GetEmailStatment(EmailSTATEMENTModel)  " +
            "wiht {@dto} {@TraceId}", new { correlationId, accountNumber, fromDate, toDate }, correlationId), ex);

                return null;
            }
        }

        #region "Fack Generation"

        private static EmailStatementDTO generateFackDTO()
        {
            var emailStatementDto = new EmailStatementDTO
            {
                BankStatementHeader = new EmailStatementHeaderDTO
                {
                    AccountNo = "1231231",
                    CheckBalanceToDate = DateTime.Now.ToShortDateString(),
                    Check_balance = "1231",
                    CodeF = "just_another_code",
                    Credit_balance = "12312",
                    CustomerAddress = "Ain Zara",
                    CustomerID = "10023",
                    CustomerName = "Osamah Test",
                    NameF = "osama developer",
                    NumberCridt = "10",
                    Numberdebtor = "20",
                    Opening_Balance = "1000",
                    PeriodFrom = DateTime.Now.Subtract(new TimeSpan(10, 0, 0, 0)).ToShortDateString(),
                    PeriodTo = DateTime.Now.ToShortDateString(),
                    ProductName = "Test Product",
                    Reserved_Amounts = "1000",
                    Total_creditor = "2000",
                    Total_debtors = "3000",
                    TypeAccount = "1"
                },

                BankStatement = new List<EmailStatementItemDTO>
                {
                    new EmailStatementItemDTO
                    {
                        Balance = "100", Cridt = "100", Depit = "0",
                        RefrenceNo = "1001",
                        ValueDate = DateTime.Now.ToShortDateString(),
                        Description = "just for testing",
                        TransctionDate = DateTime.Now.ToShortDateString()
                    },
                    new EmailStatementItemDTO
                    {
                        Balance = "100", Cridt = "100", Depit = "0",
                        RefrenceNo = "1001",
                        ValueDate = DateTime.Now.ToShortDateString(),
                        Description = "just for testing",
                        TransctionDate = DateTime.Now.ToShortDateString()
                    },
                    new EmailStatementItemDTO
                    {
                        Balance = "100", Cridt = "100", Depit = "0",
                        RefrenceNo = "1001",
                        ValueDate = DateTime.Now.ToShortDateString(),
                        Description = "just for testing",
                        TransctionDate = DateTime.Now.ToShortDateString()
                    },
                    new EmailStatementItemDTO
                    {
                        Balance = "100", Cridt = "100", Depit = "0",
                        RefrenceNo = "1001",
                        ValueDate = DateTime.Now.ToShortDateString(),
                        Description = "just for testing",
                        TransctionDate = DateTime.Now.ToShortDateString()
                    },
                    new EmailStatementItemDTO
                    {
                        Balance = "100", Cridt = "100", Depit = "0",
                        RefrenceNo = "1001",
                        ValueDate = DateTime.Now.ToShortDateString(),
                        Description = "just for testing",
                        TransctionDate = DateTime.Now.ToShortDateString()
                    },
                    new EmailStatementItemDTO
                    {
                        Balance = "100", Cridt = "100", Depit = "0",
                        RefrenceNo = "1001",
                        ValueDate = DateTime.Now.ToShortDateString(),
                        Description = "just for testing",
                        TransctionDate = DateTime.Now.ToShortDateString()
                    },
                    new EmailStatementItemDTO
                    {
                        Balance = "100", Cridt = "100", Depit = "0",
                        RefrenceNo = "1001",
                        ValueDate = DateTime.Now.ToShortDateString(),
                        Description = "just for testing",
                        TransctionDate = DateTime.Now.ToShortDateString()
                    },
                    new EmailStatementItemDTO
                    {
                        Balance = "100", Cridt = "100", Depit = "0",
                        RefrenceNo = "1001",
                        ValueDate = DateTime.Now.ToShortDateString(),
                        Description = "just for testing",
                        TransctionDate = DateTime.Now.ToShortDateString()
                    },
                    new EmailStatementItemDTO
                    {
                        Balance = "100", Cridt = "100", Depit = "0",
                        RefrenceNo = "1001",
                        ValueDate = DateTime.Now.ToShortDateString(),
                        Description = "just for testing",
                        TransctionDate = DateTime.Now.ToShortDateString()
                    },
                    new EmailStatementItemDTO
                    {
                        Balance = "100", Cridt = "100", Depit = "0",
                        RefrenceNo = "1001",
                        ValueDate = DateTime.Now.ToShortDateString(),
                        Description = "just for testing",
                        TransctionDate = DateTime.Now.ToShortDateString()
                    }
                }
            };
            //for (int i = 0; i < 4000; i++)
            //{
            //    emailStatementDto.BankStatement.Add(new EmailStatementItemDTO
            //    {
            //        Balance = "100",
            //        Cridt = "100",
            //        Depit = "0",
            //        RefrenceNo = "1001",
            //        ValueDate = DateTime.Now.ToShortDateString(),
            //        Description = "just for testingjust for testingjust for testingjust for testingjust for testing",
            //        TransctionDate = DateTime.Now.ToShortDateString()
            //    });
            //}

            return emailStatementDto;
        }

        public async Task<string> GetBalance(string correlationId, string accountNumber)
        {
            await Task.Delay(1200);
            return "123456879";
        }

        public async Task<List<BankStatement>> GetRangeAccountStatement(string correlationId, string accountNumber,
            DateTime fromDate, DateTime toDate, TransactionTypeChoice transType)
        {
            await Task.Delay(1500);
            return new List<BankStatement>() { new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
            },  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
            } ,  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
            }  };
        }

        public async Task<List<BankStatement>> GetLastAccountStatement(string correlationId, string accountNumber, int count)
        {
            await Task.Delay(1500);
            return new List<BankStatement>() { new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
            },  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
            } ,  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
            }  };
        }

        public async Task<string> GetBalance(string correlationId, string accountNumber,
            AccountType accountType = AccountType.Current)
        {
            await Task.Delay(1200);
            return "22_999_1888";
        }

        public async Task<List<BankStatement>> GetRangeAccountStatement(string correlationId, string accountNumber,
            DateTime fromDate, DateTime toDate, TransactionTypeChoice transType,
            AccountType accountType = AccountType.Current)
        {
            DateTime overlimitFromDate = new DateTime(2001, 1, 1, 0, 0, 0);
            DateTime overlimitToDate = new DateTime(2010, 1, 1, 0, 0, 0);
            DateTime correctFromDate = new DateTime(2020, 1, 1, 0, 0, 0);
            DateTime correctToDate = new DateTime(2021, 1, 1, 0, 0, 0);

            if (DateTime.Compare(fromDate, toDate) > 0)
            {
                await Task.Delay(1500);
                return new List<BankStatement>() { };
            }

            if (DateTime.Compare(fromDate, correctFromDate) >= 0 &
               DateTime.Compare(fromDate, correctToDate) <= 0 &
               DateTime.Compare(toDate, correctFromDate) >= 0 &
               DateTime.Compare(toDate, correctToDate) <= 0)
            {
                await Task.Delay(1500);
                return new List<BankStatement>() { new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    },  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } };
            }

            if (DateTime.Compare(fromDate, overlimitFromDate) >= 0 &
               DateTime.Compare(fromDate, overlimitToDate) <= 0 &
               DateTime.Compare(toDate, overlimitFromDate) >= 0 &
               DateTime.Compare(toDate, overlimitToDate) <= 0)
            {
                await Task.Delay(1500);
                return new List<BankStatement>() { new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    },  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    },  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    },  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    },  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    },  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    },  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    },  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    },  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    }, new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } ,new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
                    } , };
            }

            //if ()
            //{
            //}
            //int result = DateTime.Compare(toDate, fromDate);
            await Task.Delay(1500);
            return new List<BankStatement>() { };
        }

        public async Task<List<BankStatement>> GetLastAccountStatement(string correlationId, string accountNumber, int count,
            AccountType accountType = AccountType.Current, TransactionTypeChoice transactionTypeChoice = TransactionTypeChoice.All)
        {
            await Task.Delay(1700);
            return new List<BankStatement>() { new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
            },  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
            } ,  new BankStatement { Amount ="10.0" , Descrption ="Test" , PostDate =DateTime.Now.ToShortDateString() , Type = TransactionType.Credit,
            }  };
        }

        public Task GetAlerts()
        {
            throw new NotImplementedException();
        }

        private static List<BankNotification> notifications = null;

        async Task<List<BankNotification>> IBankInquiriesAPI.GetNotifications(string correlationId)
        {
            await Task.Delay(1000);
            if (notifications == null)
                notifications = new List<BankNotification>
                {
                    new  BankNotification {
                        NotificationId ="1",
                        UserId = 1,
                        ClassId = 1897,
                        Descrp = "TEST-01",
                        AccountNumber = "account-01",
                        PhoneNumber = "+218914040598",
                        AppId = "1",
                        Type = TransactionType.Credit,
                        Amount = 300,
                        BranchId = 4,
                        SmsSeqNo = 90911,
                        IsActivated = true,
                        BankNotifcationObj = "1"
                    },
                 //   new  BankNotification {
                 //    NotificationId ="2",
                 //    UserId = 2,
                 //    ClassId = 1897,
                 //    Descrp = "TEST-02",
                 //    AccountNumber = "account 02",
                 //    PhoneNumber = "+218926296964",
                 //    AppId = "2",
                 //    Type = TransactionType.Debit,
                 //    Amount = 40,
                 //    BranchId = 4,
                 //    SmsSeqNo = 10265,
                 //    IsActivated = true,
                 //    BankNotifcationObj = "2"
                 //},
                    new  BankNotification {
                        NotificationId ="3",
                        UserId = 3,
                        ClassId = 1897,
                        Descrp = "TEST-03",
                        AccountNumber = "account 03",
                        PhoneNumber = "+21891159490",
                     AppId = "3",
                     Type = TransactionType.Credit,
                     Amount = 1700,
                     BranchId = 4,
                     SmsSeqNo = 0,
                     IsActivated = true,
                     BankNotifcationObj = "3"
                 },
                    new  BankNotification {
                        NotificationId ="4",
                        UserId = 4,
                        ClassId = 1897,
                        Descrp = "TEST-04",
                        AccountNumber = "0404",
                        PhoneNumber = "+218913851607",
                        AppId = "4",
                        Type = TransactionType.Debit,
                        Amount = 702,
                        BranchId = 4,
                        SmsSeqNo = 4,
                        IsActivated = true,
                        BankNotifcationObj = "4"
                    },
                 //   new  BankNotification {
                 //       NotificationId ="5",
                 //       Descrp = "TEST-05",
                 //       AccountNumber = "0505",
                 //       UserId = 5,
                 //       ClassId = 1897,
                 //       PhoneNumber = "+218914040598",
                 //       AppId = "5",
                 //       Type = TransactionType.Credit,
                 //       Amount = 70,
                 //       BranchId = 4,
                 //       SmsSeqNo = 5,
                 //       IsActivated = true,
                 //       BankNotifcationObj = "5"
                 //   },
                 //   new  BankNotification {
                 //       NotificationId ="6",
                 //       UserId = 6,
                 //       ClassId = 1897,
                 //       Descrp = "TEST-06",
                 //       AccountNumber = "0606",
                 //       PhoneNumber = "+218914040598",
                 //       AppId = "6",
                 //       Type = TransactionType.Credit,
                 //       Amount = 250,
                 //       BranchId = 4,
                 //       SmsSeqNo = 6,
                 //       IsActivated = true,
                 //       BankNotifcationObj = "6"
                 //   },
                 //   new  BankNotification {
                 //       NotificationId ="7",
                 //       UserId = 7,
                 //       ClassId = 1897,
                 //       Descrp = "TEST-07",
                 //       AccountNumber = "0707",
                 //       PhoneNumber = "+218914040598",
                 //       AppId = "7",
                 //       Type = TransactionType.Credit,
                 //       Amount = 70,
                 //       BranchId = 4,
                 //       SmsSeqNo = 7,
                 //       IsActivated = true,
                 //       BankNotifcationObj = "7"
                 //   },
                 //   new  BankNotification {
                 //       NotificationId ="8",
                 //       UserId = 8,
                 //       ClassId = 1897,
                 //       Descrp = "TEST-08",
                 //       AccountNumber = "0808",
                 //       PhoneNumber = "+218914040598",
                 //       AppId = "8",
                 //       Type = TransactionType.Credit,
                 //       Amount = 70,
                 //       BranchId = 4,
                 //       SmsSeqNo = 8,
                 //       IsActivated = true,
                 //       BankNotifcationObj = "8"
                 //   },
                 //   new  BankNotification {
                 //       NotificationId ="9",
                 //       UserId = 9,
                 //       ClassId = 1897,
                 //       Descrp = "TEST-09",
                 //       AccountNumber = "0909",
                 //       PhoneNumber = "+218914040598",
                 //       AppId = "9",
                 //       Type = TransactionType.Credit,
                 //       Amount = 70,
                 //       BranchId = 4,
                 //       SmsSeqNo = 9,
                 //       IsActivated = true,
                 //       BankNotifcationObj = "9"
                 //   },
                 //   new  BankNotification {
                 //       NotificationId ="10",
                 //       UserId = 1010,
                 //       ClassId = 1897,
                 //       Descrp = "TEST-10",
                 //       AccountNumber = "1010",
                 //       PhoneNumber = "+218914040598",
                 //       AppId = "10",
                 //       Type = TransactionType.Credit,
                 //       Amount = 70,
                 //       BranchId = 4,
                 //       SmsSeqNo = 10,
                 //       IsActivated = true,
                 //       BankNotifcationObj = "10"
                 //   },
                 ////new  BankNotification {
                 //    NotificationId ="11",
                 //    UserId = 11,
                 //    ClassId = 1897,
                 //    Descrp = "TEST-11",
                 //    AccountNumber = "1111",
                 //    PhoneNumber = "+218914040598",
                 //    AppId = "11",
                 //    Type = TransactionType.Credit,
                 //    Amount = 70,
                 //    BranchId = 4,
                 //    SmsSeqNo = 11,
                 //    IsActivated = true,
                 //    BankNotifcationObj = "11"
                 //},
                 //new  BankNotification {
                 //    NotificationId ="12",
                 //    UserId = 1212,
                 //    ClassId = 1897,
                 //    Descrp = "TEST-12",
                 //    AccountNumber = "1212",
                 //    PhoneNumber = "+218914040598",
                 //    AppId = "12",
                 //    Type = TransactionType.Credit,
                 //    Amount = 70,
                 //    BranchId = 4,
                 //    SmsSeqNo = 12,
                 //    IsActivated = true,
                 //    BankNotifcationObj = "12"
                 //},
                 //new  BankNotification{
                 //    NotificationId ="13",
                 //    UserId = 13,
                 //    ClassId = 1897,
                 //    Descrp = "TEST-13",
                 //    AccountNumber = "1313",
                 //    PhoneNumber = "+218914040598",
                 //    AppId = "13",
                 //    Type = TransactionType.Debit,
                 //    Amount = 70,
                 //    BranchId = 4,
                 //    SmsSeqNo = 13,
                 //    IsActivated = true,
                 //    BankNotifcationObj = "13"
                 //},
                 //new  BankNotification {
                 //    NotificationId ="14",
                 //    UserId = 14,
                 //    ClassId = 1897,
                 //    Descrp = "TEST-14",
                 //    AccountNumber = "1414",
                 //    PhoneNumber = "+218914040598",
                 //    AppId = "14",
                 //    Type = TransactionType.Debit,
                 //    Amount = 70,
                 //    BranchId = 4,
                 //    SmsSeqNo = 14,
                 //    IsActivated = true,
                 //    BankNotifcationObj = "14"
                 //},
                 //new  BankNotification {
                 //    NotificationId ="15",
                 //    UserId = 15,
                 //    ClassId = 1897,
                 //    Descrp = "TEST-15",
                 //    AccountNumber = "1515",
                 //    PhoneNumber = "+218914040598",
                 //    AppId = "15",
                 //    Type = TransactionType.Credit,
                 //    Amount = 70,
                 //    BranchId = 4,
                 //    SmsSeqNo = 15,
                 //    IsActivated = true,
                 //    BankNotifcationObj = "15"
                 //},
                };
            return notifications.Where(x => x.IsActivated).Take(2).ToList();
        }

        public Task<List<SubscriptionTypes>> GetSubscriptionTypes()
        {
            throw new NotImplementedException();
        }

        public Task RemoveUserNotification(string correlationId, dynamic notificationProperties)
        {
            string notificationId = notificationProperties.ToString();

            notifications.SingleOrDefault(x => x.NotificationId == notificationId).IsActivated = false;
            return Task.CompletedTask;
        }

        public Task<string> GetAccountState(string correlationId, string accountNumber)
        {
            throw new NotImplementedException();
        }

        public async Task<string> GetLastSalary(string correlationId, string accountNumber)
        {
            await Task.Delay(1200);
            return "123456879";
        }

        public Task<CustomerInfoResponse> GetAccountClass(string seqNo, string bankAccountNo)
        {
            return Task.FromResult(new CustomerInfoResponse()
            {
                AccountClass = "CUHNIL",
                AccountNumber = "12345665",
                BranchId = "1",
                Currency = "LYD",
                Name = "Customer Name",
                State = State.Success,
                CurrentBalance = "1222"
            });
        }

        public Task<OperationResult> CreateServiceCharge(Clients.WAH_V2.Abstracts.ServiceChargeDto serviceChargeDto)
        {
            return Task.FromResult(OperationResult.Valid());
        }

        public Task<OperationResult> ModifyServiceCharge(Clients.WAH_V2.Abstracts.ServiceChargeDto serviceChargeRequstDTO)
        {
            return Task.FromResult(OperationResult.Valid());
        }

        public Task<OperationResult<QueryServiceResponse>> QueryServiceCharge(string accountNum)
        {
            return Task.FromResult(OperationResult<QueryServiceResponse>.Valid(new QueryServiceResponse()
            {
                Maker = "Test Maker",
                AcountNumber = "123456789",
                AuthState = "Test Auth State",
                MakerStamp = "Test Maker Stamp",
                ModNumber = "Test Mod Number",
                ServiceDetail = new List<QueryServiceDetail>()
                {
                    new()
                    {
                        OpenState = "Test Open State 1",
                        Frequency = Frequency.D,
                        Product = "Test Product 1"
                    },
                    new()
                    {
                        OpenState = "Test Open State 2",
                        Frequency = Frequency.M,
                        Product = "Test Product 2"
                    },
                    new()
                    {
                        OpenState = "Test Open State 3",
                        Frequency = Frequency.Q,
                        Product = "Test Product 3"
                    }
                }
            }));
        }

        public Task<OperationResult> UpdateNotifactionState(Clients.WAH_V2.Abstracts.UpdateNotificationStateRequest notificationStateDTO)
        {
            return Task.FromResult(OperationResult.Valid());
        }

        public Task<OperationResult<Clients.WAH_V2.Abstracts.AccountInfo>> GetNewAccountNumber(string oldAccountNumber)
        {
            var random = new Random();
            var randomNumber = new string(Enumerable.Range(0, 12).Select(_ => random.Next(10).ToString()[0]).ToArray());

            return Task.FromResult(new OperationResult<AccountInfo>(OperationResult.ResultType.Success,
                new List<string>() { },
                new AccountInfo()
                {
                    NewAccountNumber = "333" + randomNumber,
                    NewUserId = "111222342",
                    OldAccountNumber = oldAccountNumber,
                    OldUserId = "9987966"
                }));
        }

        #endregion "Fack Generation"
    }
}