from api import API
api = API()
params = {'key1': 'value1', 'key2': 'value2'}
result = api.post(_url="", _params=params, _json=True)
print(result)