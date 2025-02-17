# unistallation script

import os, sys

def display_menu(menu):
    for k, function in menu.items():
        print(k, function.__name__)

def full_uninstall():
    print("Full uninstall removes all programs this package installed")
    print("This includes Ollama, Open WebUI, the t-ui dashboard, curl, python3, and python3.12-venv")
    print("This option is not reccomended as it could remove software used in other packages on your system")
    # remove ollama
    os.system("sudo systemctl stop ollama")
    os.system("sudo systemctl disable ollama")
    os.system("sudo rm -f /etc/systemd/system/ollama.service")
    os.sytem("sudo rm -f /bin/ollama")
    # remove curl
    os.system("sudo apt remove curl -y")
    # remove Open WebUI
    os.system("rm -rf ~/.open-webui")
    # remove python3 and python3.12-venv
    os.system("sudo apt remove python3.12-venv -y")
    os.system("sudo apt remove python3")
    # remove menu scripts
    os.system("sudo rm -rf /bin/localai")
    os.system("sudo rm -rf /bin/localai.py")

def basic_uninstall():
    print("Basic uninstall is the reccomended unistallation.")
    print("it deletes Ollama, the t-ui dashboard, and Open WebUI but keeps the other software installed.")
    # remove ollama
    os.system("sudo systemctl stop ollama")
    os.system("sudo systemctl disable ollama")
    os.system("sudo rm -f /etc/systemd/system/ollama.service")
    os.sytem("sudo rm -f /bin/ollama")
    # remove menu scripts
    os.system("sudo rm -rf /bin/localai")
    os.system("sudo rm -rf /bin/localai.py")
    # remove Open WebUI
    os.system("rm -rf ~/.open-webui")

def partial_uninstall():
    print("Partial uninstall removes only the scripts that make the t-ui dashboard but keeps Ollama, Open WebUI, and the other software installed.")
    # remove menu scripts
    os.system("sudo rm -rf /bin/localai")
    os.system("sudo rm -rf /bin/localai.py")

def main():
    os.system("clear")
    functions_names = [full_uninstall, basic_uninstall, partial_uninstall, custom_uninstall]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        print('-------[Uninstall]-------')
        display_menu(menu_items)
        print('-------------------------')
        selection = int(
            input("ENTER SELECTION: "))
        selected_value = menu_items[selection]
        selected_value()


if __name__ == "__main__":
    main()
