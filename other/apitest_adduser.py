import requests
import json
from constants import *
from tools import log

url = TESTAPI_ADD_USER

payload = {
  "id": 0,
  "fullName": "أيوب",
  "phone": "",
  "emailAddress": "",
  "userName": f"{ADMIN_USERNAME}",
  "password": f"{ADMIN_PASSWORD}",
  "userType": 0,
  "permissions": 0,
  "paymentPermissions": 0,
  "branches": [0],
  "activateState": 1,
  "firstLogin": False,
  "notes": "",
  "otpSn": "{{sn}}",
  "insertedBy": 1,
  "dateInserted": "2023-03-06T10:54:12.011Z",
  "updatedBy": 1,
  "dateUpdated": "2023-03-06T10:54:12.011Z",
  "stringPermissions": ""
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    print('User created successfully.')
else:
    print('Failed to create user:', response.text)

try:
    data = response.json()
except Exception as e:
    print(e)
    data = None

if(data):
    log("RESPONSE DATA RECEIVED")
else:
    log("ERROR: COUlD NOT READ DATA RESPONSE")
    exit()

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
if(not messages):
    log(f"SUCCESS: messages={messages}")
else:
    log(f"FAILED: messages: ({messages})")

#test traceid
traceId = data["traceId"]
if(traceId):
    log(f"SUCCESS: traceId={traceId}")
else:
    log(f"FAILED: traceId: ({traceId})")


print("--------------------------------------------------")
print(response.json())


