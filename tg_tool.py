import os
import sys
import time
import requests

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear_screen()
    # Stylist Header
    print("\033[1;35m" + "="*50)
    print(r"""  ______   _    _   _____    _____   _____ _____ 
 |  ____| / \  | | |  __ \  |  __ \ |_   _|_   _|
 | |__   / _ \ | | | |  | | | |  | |  | |   | |  
 |  __| / ___ \| | | |  | | | |  | |  | |   | |  
 | |   /_/   \_\_| | |__| | | |__| | _| |_ _| |_ 
 |_|               |_____/  |_____/ |_____|_____|""")
    print("\n" + " "*17 + "FAHDII TOOLS")
    print("="*50 + "\033[0m")
    print("\033[1;36m" + "        >>> TG TO NUMBER INFO TOOL <<<" + "\033[0m")
    print("\033[1;32m" + "="*50 + "\033[0m\n")

def first_time_setup():
    banner()
    print("\033[1;33m[!] WELCOME TO FAHDII TOOLS SETUP [!]\033[0m\n")
    print("\033[1;37m1. Join WhatsApp Channel:\033[0m https://whatsapp.com/channel/0029VbCWPeh6RGJ8b9vJJv2j")
    print("\033[1;37m2. Usage:\033[0m Enter Telegram Username with or without '@'\n")
    print("\033[1;31mNote: Please make sure you have joined the channel.\033[0m")
    input("\n\033[1;32mPress ENTER to finish setup and open tool...\033[0m")
    
    # Setup marker file taake har baar setup open na ho
    with open(".setup_done", "w") as f:
        f.write("done")

def main():
    # Agar setup file nahi hai to pehle setup chalega
    if not os.path.exists(".setup_done"):
        first_time_setup()
        
    banner()
    
    # User input
    tg_id = input("\033[1;37mEnter Telegram Username (e.g. @techbyfahdii): \033[0m").strip()
    
    if not tg_id:
        print("\033[1;31m[-] Invalid Input!\033[0m")
        return

    # Auto add @ if missing
    if not tg_id.startswith('@'):
        tg_id = '@' + tg_id

    print("\n\033[1;33m[*] Fetching details from API...\033[0m")
    time.sleep(1)

    url = f"https://wasifali-telegram-id-to-number.vercel.app/api?userid={tg_id}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data.get("success") == True or data.get("success") == "true":
            print("\n\033[1;32m[+] DATA FOUND SUCCESSFULLY!\033[0m\n")
            print(f"\033[1;36mUser ID     :\033[0m {data.get('user_id')}")
            print(f"\033[1;36mCountry     :\033[0m {data.get('country')}")
            print(f"\033[1;36mCountry Code:\033[0m {data.get('country_code')}")
            print(f"\033[1;36mPhone Number:\033[0m {data.get('country_code')}{data.get('number')}")
        else:
            print("\n\033[1;31m[-] No details found or invalid Username!\033[0m")
            
    except requests.exceptions.RequestException:
        print("\n\033[1;31m[-] Connection Error! Check your internet.\033[0m")
    except ValueError:
        print("\n\033[1;31m[-] API Error or Temporary down.\033[0m")

    print("\n\033[1;32m="*50 + "\033[0m")

if __name__ == "__main__":
    main()
