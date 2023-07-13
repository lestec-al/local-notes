import socket, os, subprocess, threading
from pathlib import Path

class LogHandler(threading.Thread):
    def run(self):
        with SERVER.stdout as s:
            try:
                for line in iter(s.readline, b''):
                    print(line.decode("utf-8").strip())

            except Exception as e:
                print(str(e))

    def stop(self):
        pass

port = 8000
ip = socket.gethostbyname(socket.gethostname())
base_dir = Path(__file__).resolve().parent
link = f"http://{ip}:{port}"

env_found = False
for f in os.scandir(base_dir):
    if f.is_dir() and f.name == ".env":
        env_found = True
        break

if env_found == True:
    if os.name == 'nt':
        env_command = ".env\\Scripts\\activate.ps1"
    else:
        env_command = "source .env/bin/activate"
    final_command = f"{env_command}; python {base_dir}/manage.py runserver {ip}:{port}"
else:
    final_command = f"python {base_dir}/manage.py runserver {ip}:{port}"

SERVER = subprocess.Popen([
        "powershell",
        "-Command",
        final_command
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    shell=True
)

log = LogHandler()
log.start()
os.startfile(link)

print("Note: if something doesn't work, please repeat the installation process")

while True:
    input1 = input("COMMANDS: «exit», «link»\n")

    if input1 == "exit":
        if os.name == 'nt':
            subprocess.Popen(f"TASKKILL /F /PID {SERVER.pid} /T")
        else:
            SERVER.terminate()
        break

    elif input1 == "link":
        print(link)
        os.startfile(link)
    
    else:
        print("Unknown command")