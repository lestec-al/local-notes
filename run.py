import socket

VENV_FOLDER_NAME = ".venv"
PORT = 8000
IP = socket.gethostbyname(socket.gethostname())
LINK = f"http://{IP}:{PORT}"

# Start service
if __name__ == "__main__":
    import os, subprocess, threading
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

    base_dir = Path(__file__).resolve().parent

    # Find virtual environment
    venv_path = Path(base_dir, VENV_FOLDER_NAME)
    if venv_path.exists():
        if os.name == "nt":
            env_command = f"{venv_path}\\Scripts\\activate.ps1"
        else:
            env_command = f"source {venv_path}/bin/activate"
        final_command = f"{env_command}; python {base_dir}/manage.py runserver {IP}:{PORT}"
    else:
        final_command = f"python {base_dir}/manage.py runserver {IP}:{PORT}"

    # Run server
    SERVER = subprocess.Popen([
        "powershell" if os.name == "nt" else "gnome-terminal",
        "-Command",
        final_command
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True
    )

    log = LogHandler()
    log.start()

    print(LINK)
    try:
        os.startfile(LINK)
    except:
        pass

    while True:
        input1 = input("Commands: «exit», «link»\n")

        if input1 == "exit":
            if os.name == 'nt':
                subprocess.Popen(f"TASKKILL /F /PID {SERVER.pid} /T")
            else:
                SERVER.terminate()
            break

        elif input1 == "link":
            print(LINK)
            try:
                os.startfile(LINK)
            except:
                pass
        
        else:
            print("Unknown command")