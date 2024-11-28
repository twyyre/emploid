import requests
import json

class Testman:
    def __init__(self):
        pass

    def post(self, _url:str, _data=None, _params=None, _headers=None, _json=True):

        if(_data):
            _data=json.dumps(_data)
        
        return requests.post(url=_url, data=_data, params=_params, headers=_headers)
    
    def get(self, _url:str, _params, _headers=None, _json=True):

        return requests.get(url=_url, params=_params, headers=_headers)
    
    def post_with_header(self, _header:dict, _url:str, _data:dict):

        s = self.Session()
        # s.auth = ('user', 'pass')
        s.headers.update(_data)

        return s.post(_url, headers=_header)