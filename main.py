# -*- coding: utf-8 -*-
import os , errno , sys , subprocess
from tools.client.text_color import color




def main():
    from tools.client.client import client

    check_output = client().system('apt show version figlet')

    #client().puts(str(check_output2))
    client().system("clear")

    if check_output != 0:
        client().system("sudo apt-get install figlet")




    client().system("clear")


    client().system(f"figlet Hacking Tool Kits")


    client().puts("""

If you find a bug or bug, you can contact me on discord. cryonicx#0044 - 690517771045437530


View My Other Projects On Github:

https://github.com/CryonicsX - https://github.com/Reflechir


1: DDOS
2: Brute-Force
3: Database-Stealing
4: Exploit-Search
5: Firewall-Dedection
6: Port-Scanner
7: Toolkit-Search
8: Trojan-Maker
9: Vpn-Checker
10: Vulnerability-Analysis
0: Quit 
    """)


    CRYONICX = client().read(f"{color.GREEN}Enter transaction number {color.RESET_ALL} ")


    if CRYONICX == "1":
        client().system("python3 tools/ddos.py")

    if CRYONICX == "2":
        client().system("python3 tools/brute_force.py")

    elif CRYONICX == "3":
        client().system("python3 tools/Database_Stealing_Tool.py")

    elif CRYONICX == "4":
        client().system("python3 tools/Exploit_Search_Tool.py")

    elif CRYONICX == "5":
        client().system("python3 tools/Firewall_detection_tool.py")

    elif CRYONICX == "6":
        client().system("python3 tools/port_scanner.py")

    elif CRYONICX == "7":
        client().system("python3 tools/toolkit_search.py")

    elif CRYONICX == "8":
        client().system("python3 tools/trojan_maker.py")

    elif CRYONICX == "9":
        client().system("python3 tools/vpn_check.py")

    elif CRYONICX == "10":
        client().system("python3 tools/vulnerability_analysis.py")

    elif CRYONICX == "0":
        client().puts("""
        
        Thank You For Playing Fair :)
        
        View My Other Projects On Github:

        https://github.com/CryonicsX

        goodbye 👍👍
        
        
        """)





if __name__ == '__main__' and os.name == 'posix':
    if os.getuid() == 0:
        main()
    else:
        print(f"{color.RED}[-] Please open the program as admin or root! ( sudo python3 main.py ){color.RESET_ALL}")
        exit()
else:
    print(f"""
    
{color.GREEN}    
█░█ ▄▀█ █▀▀ █▄▀ █ █▄░█ █▀▀   ▀█▀ █▀█ █▀█ █░░   █▄▀ █ ▀█▀ █▀    Developed by CryonicX & Ref
█▀█ █▀█ █▄▄ █░█ █ █░▀█ █▄█   ░█░ █▄█ █▄█ █▄▄   █░█ █ ░█░ ▄█
{color.RESET_ALL}

{color.RED}[!] You can run this script only on debian system.{color.RESET_ALL}

        
View My Other Projects On Github:

{color.YELLOW}https://github.com/CryonicsX\n\nhttps://github.com/Reflechir{color.RESET_ALL}

goodbye 👍👍
    """)
