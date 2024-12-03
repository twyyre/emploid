from setuptools import setup

setup(
   name='emploid',
   version='0.0.8',
   description='A simple to use automation tool for automating web, android and windows proccesses.',
   long_description='A simple to use automation tool for automating web, android and windows proccesses.',
   author='PixQuilly',
   author_email='pixquilly@gmail.com',
   packages=['emploid'],  #same as name
   install_requires=['wheel', 'bar', 'greek', 'cv2', 'numpy', 'pyautogui'], #external packages as dependencies
)