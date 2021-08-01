import os , time
from client.client import client
from client.text_color import color

def main():

    client().system("clear")

    client().puts(f"""


 _______                  _      ______                                                 
|_   __ \                / |_  .' ____ \                                                
  | |__) | .--.   _ .--.`| |-' | (___ \_| .---.  ,--.   _ .--.   _ .--.  .---.  _ .--.   github.com/CryonicsX
  |  ___// .'`\ \[ `/'`\]| |    _.____`. / /'`\]`'_\ : [ `.-. | [ `.-. |/ /__\\[ `/'`\] 
 _| |_   | \__. | | |    | |,  | \____) || \__. // | |, | | | |  | | | || \__., | |     
|_____|   '.__.' [___]   \__/   \______.''.___.'\'-;__/[___||__][___||__]'.__.'[___] 


1: Level 1 scanning
2: Level 2 scanning
3: Level 3 scanning
4: MENU
""")
    get_input = client().read(f"{color.GREEN}Please make a selection{color.RESET_ALL} ")


    if get_input == "1":
        viktim_ip = client().read(f"{color.GREEN}Enter target IP{color.RESET_ALL} ")
        client().puts(f"{color.GREEN}[✔] Starting ...{color.RESET_ALL}")
        time.sleep(2.5)
        client().system(f"nmap {viktim_ip}")

    
    elif get_input == "2":
        viktim_ip = client().read(f"{color.GREEN}Enter target IP{color.RESET_ALL} ")
        client().puts(f"{color.GREEN}[✔] Starting ...{color.RESET_ALL}")
        time.sleep(2.5)
        client().system(f"nmap -sS -sV - {viktim_ip}")

    
    elif get_input == "3":
        viktim_ip = client().read(f"{color.GREEN}Enter target IP{color.RESET_ALL} ")
        client().puts(f"{color.GREEN}[✔] Starting ...{color.RESET_ALL}")
        time.sleep(2.5)
        client().system(f"nmap -0 {viktim_ip}")

    elif get_input == "4":
        client().system("python3 main.py")

    else:
        client().puts(f"{color.RED}[!] Make a valid choice. 1 , 2 , 3{color.RESET_ALL}")


    returnED = client().read(f"{color.GREEN} Do you want to make a new scann?(Y/N) {color.RESET_ALL}").lower()

    if returnED == "y":
        client().system("python tools/port_scanner.py")


    elif returnED == "n":
        client().puts(f"""
View My Other Projects On Github:

{color.YELLOW}https://github.com/CryonicsX\n\nhttps://github.com/Reflechir{color.RESET_ALL}

goodbye 👍👍
        """)
        exit()


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
