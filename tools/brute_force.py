import os , time
from client.client import client
from client.text_color import color

def main():
    
    client().system("clear")

    client().system(f"figlet Brute Force")

    client().puts(f"Welcome to Brute Force Tool\n\ngithub.com/CryonicsX")

    client().puts(f"""    
    1: FTP
    2: SSH
    3: MENU
    """)

    get_input = client().read(f"Please make a selection ")



    if get_input == "1":
        viktim = client().read(f"Enter Target IP{color.RESET_ALL} ")
        word_list_username = client().read(f"{color.GREEN}Enter the role of the username.txt file ")
        word_list_password = client().read(f"{color.GREEN}Enter the role of the password.txt file ")

        client().puts(f"{color.GREEN}[✔] Starting ...{color.RESET_ALL}")
        time.sleep(2.5)
        client().system(f"nerack -P.21 -u {word_list_username} - p {word_list_password} {viktim}")
    
    elif get_input == "2":
        viktim = client().read(f"Enter Target IP{color.RESET_ALL} ")
        word_list_username = client().read(f"{color.GREEN}Enter the role of the username.txt file ")
        word_list_password = client().read(f"{color.GREEN}Enter the role of the password.txt file ")
        
        client().puts(f"{color.GREEN}[✔] Starting ...{color.RESET_ALL}")
        time.sleep(2.5)
        client().system(f"nerack -P.22 -u {word_list_username} - p {word_list_password} {viktim}")

    elif get_input == "3":
        client().system("python3 main.py")


    else:
        client().puts(f"{color.RED}[!] No such transaction found{color.RESET_ALL}")


    returnED = client().read(f"{color.GREEN} Do you want to make a new Brute Force?(Y/N) {color.RESET_ALL}").lower()

    if returnED == "y":
        client().system("python3 tools/brute_force.py")


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
    {color.RESET_ALL}""")
