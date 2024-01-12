from appium import webdriver
from flutter_driver import FlutterDriver

desired_caps = {
    'platformName': 'flutter',
    'deviceName': 'flutter',
    'headless': False
}

appium_driver = webdriver.Remote('https://chat.openai.com/c/840d220e-daba-4613-a2fc-700b4b6046c4', desired_caps)
flutter_driver = FlutterDriver(appium_driver)

try:
    # Your Flutter Driver test code goes here
    # Execute JavaScript code
    result = appium_driver.execute_script('return document.title;')
    print(f'Page title: {result}')
except Exception as e:
    print("an exception occured")
    print("exception:", e)

finally:
    flutter_driver.close()