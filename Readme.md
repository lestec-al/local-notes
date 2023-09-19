# Local Notes App
A simple app for sharing notes with multiple devices on a local network. For example, write a text on a PC and continue on a phone or other device on the same network. It can also be a base for developing your own app.

<img src="https://github.com/lestec-al/local-notes/raw/main/pic1.png" width="640" height="360"/>
<img src="https://github.com/lestec-al/local-notes/raw/main/pic2.png" width="450" height="340"/>


# Installation for Windows:
- install Python (I use v3.11 but from v3.9 should work)
- download or clone this repo and in the project folder run via command line
    - `pip install -r requirements.txt`
    - `python manage.py makemigrations`
    - `python manage.py migrate`


# Launching on Windows:
- launch file 'run.bat'
- if 'run.bat' doesn't work try:
    - open a command prompt and select the project folder through it
    - type command `python run.py`