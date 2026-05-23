import os
import sys
import time
import requests
import subprocess

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear_screen()
    # New Futuristic Premium Design Banner
    print("\033[1;36m" + "⚡ " + "="*46 + " ⚡")
    print(r"""\033[1;35m    _______ ___   _   _ ______  _____ _____ 
   |  _____/   \ | | | |  __  \|_   _|_   _|
   | |__  / _ \ \| |_| | |  |  | | |   | |  
   |  __|/ ___ \ \  _  | |  |  | | |   | |  
   | |  /_/     \_\_| |_| |__|  |_| |_ _| |_ 
   |_|                  |______/|_____|_____|""")
    print("\033[1;36m" + "⚡ " + "="*46 + " ⚡\033[0m")
    print(" "*16 + "\033[1;32m[ DEVELOPED BY FAHAD ]\033[0m\n")

def open_whatsapp():
    channel_url = "https://whatsapp.com/channel/0029VbCWPeh6RGJ8b9vJJv2j"
    print("\n\033[1;35m[*] Connecting to secure link redirector...\033[0m")
    time.sleep(1)
    print("\033[1;32m[+] Opening WhatsApp Channel in Browser!\033[0m")
    time.sleep(0.5)
    # Background execution without showing link on Termux terminal
    subprocess.run(["termux-open", channel_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def info_tool():
    banner()
    print("\033[1;33m┌──────────────────────────────────────────────┐")
    print("│         >>> TG TO NUMBER INFO TOOL <<<       │")
    print("└──────────────────────────────────────────────┘\033[0m\n")
    
    tg_id = input("\033[1;37mEnter Telegram Username (e.g. @techbyfahdii): \033[0m").strip()
    
    if not tg_id:
        print("\n\033[1;31m[-] Invalid Input!\033[0m")
        return

    if not tg_id.startswith('@'):
        tg_id = '@' + tg_id

    print("\n\033[1;35m[*] Fetching details from API server...\033[0m")
    time.sleep(1.5)

    url = f"https://wasifali-telegram-id-to-number.vercel.app/api?userid={tg_id}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data.get("success") == True or data.get("success") == "true":
            print("\n\033[1;32m[+] DATA RETRIEVED SUCCESSFULLY!\033[0m\n")
            print(f"\033[1;36m 🌐 User ID      :\033[0m {data.get('user_id')}")
            print(f"\033[1;36m 📍 Country      :\033[0m {data.get('country')}")
            print(f"\033[1;36m 🔑 Country Code :\033[0m {data.get('country_code')}")
            print(f"\033[1;36m 📞 Phone Number :\033[0m {data.get('country_code')}{data.get('number')}")
        else:
            print("\n\033[1;31m[-] No details found or invalid Username!\033[0m")
            
    except requests.exceptions.RequestException:
        print("\n\033[1;31m[-] Connection Error! Please check your network.\033[0m")
    except ValueError:
        print("\n\033[1;31m[-] API Response Error or Server Maintenance.\033[0m")

    print("\n\033[1;36m" + "="*50 + "\033[0m")
    print("\033[1;32mteach by Fardeen tools\033[0m") # Signature added

def main():
    banner()
    # Cyberpunk style box interface
    print("\033[1;34m┌──────────────────────────────────────────────┐")
    print("\033[1;37m│  \033[1;32m[1]\033[1;37m JOIN CHANNEL (Direct Open Links)        │")
    print("\033[1;37m│  \033[1;32m[2]\033[1;37m TG TO NUMBER INFO SYSTEM                │")
    print("\033[1;34m└──────────────────────────────────────────────┘\033[0m\n")
    
    choice = input("\033[1;33m⚡ Reply Choice (1 or 2): \033[0m").strip()
    
    if choice == "1":
        open_whatsapp()
    elif choice == "2":
        info_tool()
    else:
        print("\n\033[1;31m[-] Invalid Choice! System shutting down.\033[0m")

if __name__ == "__main__":
    main()
	
