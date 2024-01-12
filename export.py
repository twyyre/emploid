import PyInstaller.__main__

PyInstaller.__main__.run([
    'emp_test.py',
    '--onefile',
    '--windowed',
    '--icon=emplogo.png'  # Replace 'your_icon_path.ico' with the actual path to your icon file
])
