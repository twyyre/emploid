import requests

class API:

    def __init__(self):
        self.get = staticmethod(self.get)
        self.post = staticmethod(self.post)
        
    def get(_url, _params=None, _json=True):
        # _params = {'key1': 'value1', 'key2': 'value2'}
        if(_json):
            return requests.get(_url, params=_params).json()
        else:
            return requests.get(_url, params=_params)

    def post(_url, _params=None, _json=True):
        # _params = {'key1': 'value1', 'key2': 'value2'}
        if(_json):
            return requests.post(_url, params=_params).json()
    
        
    
