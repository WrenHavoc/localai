# A T-ui interface for managing your local ai

import os, time, sys

def display_menu(menu):
    for k, function in menu.items():
        print(k, function.__name__)

def ollama_start():
    os.system("ollama serve")

def ollama_download():
    print("go to https://ollama.com/search in your browser to pick a model")
    model = input("model to install: ")
    os.system("ollama pull " + model)

def open_webui():
    os.system("gnome-terminal -- ~/open-webui-venv/bin/open-webui serve")
    time.sleep(5)
    os.system("firefox 127.0.0.1:8080")

def done():
    sys.exit()

def main():
    os.system("clear")
    functions_names = [ollama_start, ollama_download, open_webui, done]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        print("----------[AI Dashboard]----------")
        display_menu(menu_items)
        print("----------------------------------")
        selection = int(input("Select Item: "))
        selected_value = menu_items[selection]
        selected_value()

if __name__ == "__main__":
    main()
