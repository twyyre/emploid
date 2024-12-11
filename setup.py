from setuptools import setup
from charset_normalizer import detect

def process_requirements(_fname="requirements.txt"):
   try:
        with open(_fname, "rb") as f:
            byte_content = f.read()
            detected = detect(byte_content)
            encoding = detected.get("encoding", "utf-8")  # Default to utf-8 if detection fails
            content = byte_content.decode(encoding)
            return [
               line.strip() for line in content.splitlines()
               if line.strip() and not line.startswith("#")
            ]
   except Exception as e:
      print(f"Error reading requirements file: {e}")
      return []

setup(
   name='emploid',
<<<<<<< HEAD
   version='0.4.8',
=======
   version='0.4.10',
>>>>>>> a1047ea8b9bdf95d79bd01b7a2a800e1995af0f7
   description='A simple to use automation tool for automating web, android and windows proccesses.',
   long_description='A simple to use automation tool for automating web, android and windows proccesses.',
   author='PixQuilly',
   author_email='pixquilly@gmail.com',
   packages=['emploid'],  #same as name
   install_requires=process_requirements(), #external packages as dependencies
)