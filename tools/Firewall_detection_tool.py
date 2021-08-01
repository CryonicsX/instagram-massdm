import os , time
from client.client import client
from client.text_color import color

def main():

    client().system("clear")

    client().system(f"figlet Firewall Detection")

    client().puts(f"Welcome to Firewall Detection Tool\n\ngithub.com/CryonicsX\n\n")

    client().puts("""
1: Start the Script
2: MENU
    
    """)

    selection = client().read(f"Enter transaction number ")

    if selection == "1":

        viktim = client().read(f"{color.GREEN}Enter Target Site Adress{color.RESET_ALL} ")
        client().puts(f"{color.GREEN}[✔] Starting ...{color.RESET_ALL}")
        time.sleep(2.5)
        client().system(f"wafw00f {viktim}")


    elif selection == "2":
        client().system("python3 main.py")

    else:
        client().puts("There is no such option")

    returnED = client().read(f"{color.GREEN} Do you want to make a new search?(Y/N) {color.RESET_ALL}").lower()

    if returnED == "y":
        client().system("python3 tools/Firewall_detection_tool.py")


    elif returnED == "n":
        client().puts(f"""
View My Other Projects On Github:

{color.YELLOW}https://github.com/CryonicsX\n\nhttps://github.com/Reflechir{color.RESET_ALL}

goodbye 👍👍
        """)

    else:
        client().puts("There is no such option")

    
    
if __name__ == '__main__' and os.name == 'posix':
    if os.getuid() == 0:
        main()
else:
    client().puts(f"""
    
{color.GREEN}    
█░█ ▄▀█ █▀▀ █▄▀ █ █▄░█ █▀▀   ▀█▀ █▀█ █▀█ █░░   █▄▀ █ ▀█▀ █▀    Developed by CryonicX & Ref
█▀█ █▀█ █▄▄ █░█ █ █░▀█ █▄█   ░█░ █▄█ █▄█ █▄▄   █░█ █ ░█░ ▄█
{color.RESET_ALL}

{color.RED}[!] You can run this script only on debian system.{color.RESET_ALL}

        
View My Other Projects On Github:

{color.YELLOW}https://github.com/CryonicsX\n\nhttps://github.com/Reflechir{color.RESET_ALL}

goodbye 👍👍
    """)
