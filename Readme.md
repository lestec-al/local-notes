# Local Notes App
A simple app for sharing notes with multiple devices on a local network. For example, write a text on a PC and continue on a phone or other device on the same network. It can also be a base for developing your own app.

<img src="https://github.com/lestec-al/local-notes/raw/main/pic1.png" width="640" height="360"/>
<img src="https://github.com/lestec-al/local-notes/raw/main/pic2.png" width="450" height="340"/>


# Installation:
- install Python (I use v3.11 but from v3.9 should work) https://www.python.org/downloads/
- download and unpack (or get in other ways) this project
- open a command prompt (eg. powershell, terminal) and select the project folder through it (eg. 'cd <path/to/folder>')
- type commands (see how to run python commands on your OS, the first word can be different, eg. for some Linux-es 'python3 -m venv .venv'):
    - python -m venv .venv
    - '.venv\Scripts\activate' (windows) or 'source .venv/bin/activate' (linux, mac)
    - pip install -r requirements.txt (all OS)
    - python manage.py makemigrations
    - python manage.py migrate


# Launching:
- launch file 'run.bat'
- if 'run.bat' doesn't work try:
    - open a command prompt and select the project folder through it
    - type command 'python run.py'