import requests
from time import sleep
from statistics import median

def test_func(*args):
    print("this is a testing function.")

def send_post(*args):
    request_number = 1
    i = 0
    delay = 0
    request_time_list = []

    while i<=request_number:
        i+=1
        print(f"request number ({i})")
        base_url = "https://wattpad.com"
        endpoint="/"
        #
        username="shewa"
        password="1111111a"
        otp=""

        #
        test_url = base_url+endpoint
        data_obj = {
            "userName": username,
            "password": password,
            "Otp": otp
        }
        request = requests.post(url=test_url, json=data_obj)#, data=data_obj)

        request_time = request.elapsed.total_seconds()
        request_time_list.append(request_time)

        result = request.json()
        try:
            result = result["content"]["value"]
            print(result)
            print(f"response time: {request_time}")

        except Exception as e:
            print("getting result failed")

        if(delay):
            sleep(delay)

    median_value = median(request_time_list)
    print(f"median of request times is ({median_value})")

def send_get(_request_number, _ddd):
    request_number = _request_number
    i = 0
    delay = 0
    request_time_list = []

    while i < request_number:
        i+=1
        # print(f"request number ({i})")
        base_url = "https://itameios.com"
        endpoint="/"

        request = requests.get(url=base_url)#, data=data_obj)

        print(f"{_ddd} -- {request}")

        request_time = request.elapsed.total_seconds()
        request_time_list.append(request_time)

        
        try:
            result = request.json()
            result = result
            # print(result)
            # print(f"response time: {request_time}")

        except Exception as e:
            # print("getting result failed")
            pass

        if(delay):
            sleep(delay)

    median_value = median(request_time_list)
    # print(f"median of request times is ({median_value})")


