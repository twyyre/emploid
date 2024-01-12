import requests
from constants import *
from tools import log
import json
from tools import wait

class Testman:
    def __init__(self):
        pass

    def post(self, _url:str, _data=None, _params=None, _headers=None):
        if(_data):
            _data=json.dumps(_data)
        
        return requests.post(url=_url, data=_data, params=_params, headers=_headers)
    
    def get(self, _url:str, _params, _headers=None):
        return requests.get(url=_url, params=_params, headers=_headers)
    
    def post_with_header(self, _header:dict, _url:str, _data:dict):
        s = self.Session()
        # s.auth = ('user', 'pass')
        s.headers.update(_data)

        return s.post(_url, headers=_header)
    
    def create_user(self, _username=ADMIN_USERNAME, _password=ADMIN_PASSWORD, _type=0):
        #create ADMIN user
        log("create user", _heading=True)
        params = {
            "id": 0,
            "fullName": "أيوب",
            "phone": "",
            "emailAddress": "",
            "userName": f"{_username}",
            "password": f"{_password}",
            "userType": _type,
            "permissions": 0,
            "paymentPermissions": 0,
            "branches": [
                0
            ],
            "activateState": 1,
            "firstLogin": False,
            "notes": "",
            "otpSn": f"{SN}",
            "insertedBy": 1,
            "dateInserted": "2023-03-06T10:54:12.011Z",
            "updatedBy": 1,
            "dateUpdated": "2023-03-06T10:54:12.011Z",
            "stringPermissions": ""
        }

        headers = {'Content-Type': 'application/json'}
        response = self.post(_url=TESTAPI_ADD_USER, _data=params, _headers=headers)
        
        #test response
        data = self.test_response(response)

        #test status code for 200 ok
        if(self.test_status(response.status_code)):
            pass
        else:
            pass

        #test type for 1
        if(self.test_type(_actual_type=data["type"], _expected_type=1)):
            pass
        else:
            pass

        #test messages
        if(self.test_messages(data["messages"])):
            pass
        else:
            pass

        #test traceid
        traceid = data["traceId"]
        if(self.test_traceid(traceid)):
            pass
        else:
            pass

    def delete_user(self, _username=ADMIN_USERNAME):
        #delete ADMIN user
        log("delete user", _heading=True)
        params = {
            'username': _username,
            'culture': 'ar-LY',
        }
        response = self.get(_url=TESTAPI_DELETE_USER, _params=params)

        #test response
        data = self.test_response(response)

        #test status code for 200 ok
        if(response.status_code==200):
            log(f"SUCCESS: STATUS={response.status_code}")
        else:
            log(f"FAILED: STATUS={response.status_code}")

        #test type for 1
        type_code = data["type"]
        if(type_code==1):
            log(f"SUCCESS: type={type_code}")
        else:
            log(f"FAILED: type={type_code}")

        #test messages
        messages = data["messages"]
        if(messages):
            log(f"SUCCESS: messages={messages}")
        else:
            log(f"FAILED: messages: ({messages})")

        #test traceid
        traceId = data["traceId"]
        if(traceId):
            log(f"SUCCESS: traceId={traceId}")
        else:
            log(f"FAILED: traceId: ({traceId})")


    def set_sn_state(self, _sn=SN, _state=1):
        #set admin SN state to reserved so we can log in with it
        log("set admin sn state", _heading=True)
        params = {
            'Sn': _sn,
            'state': _state,
            'culture': 'ar-LY',
        }
        response = self.get(_url=TESTAPI_SET_SN_STATE, _params=params)

        #test status code for 200 ok
        if(self.test_status(response.status_code)):
            pass
        else:
            pass
            
        #test response
        data = self.test_response(response)

        #test type for 1
        if(self.test_type(_actual_type=data["type"], _expected_type=1)):
            pass
        else:
            pass

        #test messages
        if(self.test_messages(data["messages"])):
            pass
        else:
            pass

        #test traceid
        traceid = data["traceId"]
        if(self.test_traceid(traceid)):
            pass
        else:
            pass


    def get_otp(self, _sn=SN):
        #get otp 
        log("get otp", _heading=True)
        params = {
            'sn': _sn,
            'culture': 'ar-LY',
        }
        response = self.get(_url=TESTAPI_GET_OTP, _params=params)

        #test response
        data = self.test_response(response)

        #test status code for 200 ok
        if(response.status_code==200):
            log(f"SUCCESS: STATUS={response.status_code}")
        else:
            log(f"FAILED: STATUS={response.status_code}")

        OTP = str(data)
        log(f"otp: {OTP}")

        return OTP

    def get_user_id(self, _username=ADMIN_USERNAME):
        #get admin id
        log("get user id", _heading=True)
        params = {
            'searchTerm': _username,
            'searchOptions': 1,
            'culture': 'ar-LY',
        }
        response = self.get(_url=TESTAPI_GET_USER_ID, _params=params)

        #test response
        data = self.test_response(response)

        #test status code for 200 ok
        if(self.test_status(response.status_code)):
            pass
        else:
            pass

        #test type for 1
        if(self.test_type(_actual_type=data["type"], _expected_type=1)):
            pass
        else:
            pass

        #test messages
        if(self.test_messages(data["messages"])):
            pass
        else:
            pass

        #test traceid
        traceid = data["traceId"]
        if(self.test_traceid(traceid)):
            pass
        else:
            pass

        id = data["content"]["id"]

        log("userid:", id)
        return id

    def user_signin(self, _username=ADMIN_USERNAME, _password=ADMIN_PASSWORD, _otp=OTP):
        #sign in with admin so we can authenticate 
        log("sign in", _heading=True)
        params = {
            'userName': _username,
            'password': _password,
            'otp': _otp,
            'culture': 'ar-LY'
        }
        headers = {'Content-Type': 'application/json'}
        response = self.post(_url=TESTAPI_BACK_SIGNIN, _data=params, _headers=headers)

        #test response
        data = self.test_response(response)

        #test status code for 200 ok
        if(self.test_status(response.status_code)):
            pass
        else:
            pass

        #test type for 1
        if(self.test_type(_actual_type=data["type"], _expected_type=1)):
            pass
        else:
            pass

        #test messages
        if(self.test_messages(data["messages"])):
            pass
        else:
            pass

        #get JWT
        jwt = None
        try:
            jwt = data["content"]["value"]
            if(jwt):
                log(f"SUCCESS: jwt: ({jwt})")
            else:
                log(f"FAILED: jwt: ({jwt})")
            
        except:
            log(f"FAILED: jwt: (None)")

        wait(6) #so that we can get the log

        #test traceid
        traceid = data["traceId"]
        if(self.test_traceid(traceid)):
            TRACEID = traceid
            self.test_log(_traceid=TRACEID, _token=jwt)
        else:
            log(f"FAILED: traceid: (None)")

        userid = self.get_user_id(_username=_username)
        self.test_event(_userid=userid)

        return jwt

    def set_user_sn(self, _userid, _sn, _token=JWT):

        #set user sn
        log("set user sn", _heading=True)
        params = {
            'userId': _userid,
            'otpSn': _sn,
            'culture': 'ar-LY'
        }
        headers = {
            'Authorization': f'Bearer {_token}', 
            'Content-Type': 'application/json'
        }
        response = self.post(_url=TESTAPI_SET_USER_SN, _data=None, _params=params, _headers=headers)

        #test response
        data = self.test_response(response)

        #test status code for 200 ok
        if(self.test_status(response.status_code)):
            pass
        else:
            pass

        #test type for 1
        if(self.test_type(_actual_type=data["type"], _expected_type=1)):
            pass
        else:
            pass

        #test messages
        if(self.test_messages(data["messages"])):
            pass
        else:
            pass

        #test traceid
        traceid = data["traceId"]
        if(self.test_traceid(traceid)):
            pass
        else:
            pass

    def replace_user_sn(self, _userid, _sn, _token=JWT):

        #set user sn
        log("replace user sn", _heading=True)
        params = {
            'userId': _userid,
            'newOtp': _sn,
            'culture': 'ar-LY'
        }
        headers = {
            'Authorization': f'Bearer {_token}', 
            'Content-Type': 'application/json'
        }
        response = self.post(_url=TESTAPI_REPLACE_USER_SN, _data=None, _params=params, _headers=headers)

        #test response
        data = self.test_response(response)

        #test status code for 200 ok
        if(self.test_status(response.status_code)):
            pass
        else:
            pass

        #test type for 1
        if(self.test_type(_actual_type=data["type"], _expected_type=1)):
            pass
        else:
            pass

        #test messages
        if(self.test_messages(data["messages"])):
            pass
        else:
            pass

        #test traceid
        traceid = data["traceId"]
        if(self.test_traceid(traceid)):
            pass
        else:
            pass

    def otp_signin(self, _userid, _otp, _token=JWT):

        log("signin with otp", _heading=True)
        params = {
            'userId': _userid,
            'otp': _otp,
            'culture': 'ar-LY'
        }
        headers = {
            'Authorization': f'Bearer {_token}', 
            'Content-Type': 'application/json'
        }
        response = self.post(_url=TESTAPI_OTP_SIGNIN, _data=None, _params=params, _headers=headers)

        #test response
        data = self.test_response(response)

        #test status code for 200 ok
        if(self.test_status(response.status_code)):
            pass
        else:
            pass

        #test type for 1
        if(self.test_type(_actual_type=data["type"], _expected_type=1)):
            pass
        else:
            pass

        #test messages
        if(self.test_messages(data["messages"])):
            pass
        else:
            pass

        #test traceid
        traceid = data["traceId"]
        if(self.test_traceid(traceid)):
            pass
        else:
            pass

        #get JWT
        jwt = None
        try:
            jwt = data["content"]["value"]
            if(jwt):
                log(f"SUCCESS: jwt: ({jwt})")
            else:
                log(f"FAILED: jwt: ({jwt})")
            return jwt
        except:
            log(f"FAILED: jwt: (None)")

        return jwt
    
    def get_merchant_by_name(self, _account_no, _account_type, _branch_id, _token=JWT):

        log("get merchant by name", _heading=True)
        params = {
            'accountNo': _account_no,
            'accountType': _account_type,
            'branchId': _branch_id,
            'culture': 'ar-LY'
        }
        headers = {
            'Authorization': f'Bearer {_token}', 
            'Content-Type': 'application/json'
        }
        response = self.post(_url=TESTAPI_GET_MERCHANT_BY_NAME, _data=None, _params=params, _headers=headers)

        #test response
        data = self.test_response(response)

        #test status code for 200 ok
        if(self.test_status(response.status_code)):
            pass
        else:
            pass

        #test type for 1
        if(self.test_type(_actual_type=data["type"], _expected_type=1)):
            pass
        else:
            pass

        #test messages
        if(self.test_messages(data["messages"])):
            pass
        else:
            pass

        #test traceid
        traceid = data["traceId"]
        if(self.test_traceid(traceid)):
            pass
        else:
            pass

        #get JWT
        jwt = None
        try:
            jwt = data["content"]["value"]
            if(jwt):
                log(f"SUCCESS: jwt: ({jwt})")
            else:
                log(f"FAILED: jwt: ({jwt})")
            return jwt
        except:
            log(f"FAILED: jwt: (None)")

        return jwt
    
    def test_log(self, _traceid, _token):

        log("test log", _heading=True)
        params = {
            'traceId': _traceid,
            'culture': 'ar-LY'
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = self.get(_url=TESTAPI_GET_LOG, _params=params, _headers=headers)

        #test response
        try:
            data = self.test_response(response)[0]
        except:
            data = None

        #test status code for 200 ok
        if(self.test_status(response.status_code)):
            pass
        else:
            pass

        return data
    
    def test_event(self, _userid):

        log("test event", _heading=True)
        log("userid:", _userid)
        params = {
            'userId': _userid,
            'culture': 'ar-LY'
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = self.get(_url=TESTAPI_GET_EVENTS, _params=params, _headers=headers)

        #test response
        data = self.test_response(response)

        #test status code for 200 ok
        if(self.test_status(response.status_code)):
            pass
        else:
            pass
        
        log("number of rows:", len(data["content"]))
        
        log(data["content"][-1])

        return data
    
    def test_status(self, _actual_status, _expected_status=200):
        #test status code for 200 ok
        if(_actual_status==_expected_status):
            log(f"SUCCESS: STATUS={_actual_status}")
            return True
        else:
            log(f"FAILED: STATUS={_actual_status}")
            return False
    
    def test_type(self, _actual_type, _expected_type=1):
        #test type for 1
        type_code = _actual_type
        if(type_code==_expected_type):
            log(f"SUCCESS: type={type_code}")
            return True
        else:
            log(f"FAILED: type={type_code}")
            return False
        
    def test_messages(self, _actual_messages, _expected_messages=""):
        messages = _actual_messages
        if(messages):
            if(not _expected_messages):
                log(f"SUCCESS: messages={messages}")
            else:
                if(_expected_messages in messages):
                    log(f"SUCCESS: messages={messages}")
                else:
                    log(f"FAILED: messages: ({messages})")
        else:
            log(f"FAILED: messages: ({messages})")

    def test_traceid(self, _actual_traceid):
        traceId = _actual_traceid
        if(traceId):
            log(f"SUCCESS: traceId={traceId}")
            return True
        else:
            log(f"FAILED: traceId: ({traceId})")
            return False

    def test_response(self, _response):
        response = _response
        try:
            try:
                data = response.json()
            except:
                log("RESPONSE IS CONTENT INSTEAD OF JSON")
                data = response.content
        except Exception as e:
            print(e)
            data = None

        if(data):
            log("RESPONSE DATA RECEIVED")
            return data
        else:
            log("ERROR: COUD NOT READ DATA RESPONSE")
            pass
