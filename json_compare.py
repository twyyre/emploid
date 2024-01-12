def find_different_keys(dict1, dict2):
    different_keys = []
    for key in dict1:
        if key not in dict2 or dict1[key] != dict2[key]:
            different_keys.append(key)
    for key in dict2:
        if key not in dict1:
            different_keys.append(key)
    if(not different_keys):
        different_keys = "identical objects"
    return different_keys

# Sample dictionaries
dict1 = {

{"user":{
    "FullName":"أيوب",
    "Phone":"",
    "EmailAddress":"",
    "UserName":"Ayoub",
    "Password":"1111111Aa",
    "UserType":0,
    "Permissions":127,
    "PaymentPermissions":0,
    "Branches":[1],     
    "OtpSn":"797693694"}
}
}

# Sample dictionaries
dict2 = {

    "FullName":"أيوب",
    "Phone":"",
    "EmailAddress":"",
    "UserName":"Ayoub and another username",
    "Password":"1111111Aa",
    "UserType":0,
    "Permissions":127,
    "PaymentPermissions":0,
    "Branches":[1],
    "OtpSn":"797693694"
}

print(find_different_keys(dict1, dict2))
