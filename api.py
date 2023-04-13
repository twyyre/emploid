import requests

class API:

    def __init__(self):
        self.get = staticmethod(self.get)
        self.post = staticmethod(self.post)
        
    def get(self, _url, _params=None, _json=True):
        # _params = {'key1': 'value1', 'key2': 'value2'}
        result = requests.get(_url, params=_params)
        if(_json):
            result = result.json()
        return result

    def post(self, _url, _params=None, _json=True):
        # _params = {'key1': 'value1', 'key2': 'value2'}
        result = requests.post(_url, params=_params)
        if(_json):
            result = result.json()
        return result
    
    def delete_user_by_username(self, _username, _json=True):
        # params = {
        #     "type": 1,
        #     "messages": [
        #     "string"
        #     ],
        #     "traceId": "string"
        # }
        return self.get(_url=f"http://10.10.20.46:9832/Pages/DeleteUserByUsername?username={_username}&culture=ar-LY", _json=_json)
    
    def update_user(self, _json=True):
        params = {
            "id": 0,
            "fullName": "string",
            "phone": "string",
            "emailAddress": "string",
            "userName": "string",
            "password": "string",
            "userType": 0,
            "permissions": 0,
            "paymentPermissions": 0,
            "branches": [
                0
            ],
            "activateState": 0,
            "firstLogin": True,
            "notes": "string",
            "otpSn": "string",
            "insertedBy": 0,
            "dateInserted": "2023-03-14T07:38:56.491Z",
            "updatedBy": 0,
            "dateUpdated": "2023-03-14T07:38:56.491Z",
            "stringPermissions": "string"
            }
        return self.post(_url="http://10.10.20.46:9832/Pages/UpdateUser?culture=ar-LY", _params=params, _json=_json)
        
    
