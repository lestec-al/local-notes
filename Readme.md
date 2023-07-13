# Local Notes App
A app for sharing notes with multiple devices on a local network. For example, write a text on a PC and continue on a phone or other device on the same network.

<img src="https://github.com/lestec-al/local-notes/raw/main/pic1.png" width="640" height="360"/>
<img src="https://github.com/lestec-al/local-notes/raw/main/pic2.png" width="640" height="360"/>

# Installation:
- install Python, note:
    - I'm using Windows 10 and haven't tested the app on Linux or Mac, but it should work. Only instead of the word 'python' in commands you may need to use 'python3'. See how to install and use Python on your system
    - I'm using Python v3.11 (didn't check others) but everything from v3.9 should work
- download or clone this project
- open a command prompt (eg. powershell, terminal) and select the project folder through it (eg. 'cd <folder_name>' command)
- (optional) create virtual environment by typing commands:
    - python -m venv .env
    - '.env\Scripts\activate.ps1' (for windows) or 'source .env/bin/activate' (for unix)
- type commands:
    - pip install django
    - python manage.py makemigrations
    - python manage.py migrate


# Launching:
- launch file run.bat (tested on Windows 10)
- (optional) if 'run.bat' doesn't work try:
    - open a command prompt and select the project folder through it
    - type command 'python run.py'