import requests
import os
from colorama import Fore, Style

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + r'''
░▒▓█▓▒░▒▓███████▓▒░       ░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░▒▓███████▓▒░       ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░▒▓█▓▒░             ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░        
                                                                                                         
                                                                                                         
    [1]  Look ip               [2]  exit
    ''')
    choice = input("Choose an option: ")
    if choice == '1':
        ip_lookup()
    elif choice == '2':
        exit()
    else:
        print("Invalid option. Please try again.")
        main()

def ip_lookup():
    os.system('cls' if os.name == 'nt' else 'clear')
    ip = input(f"Enter IP: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Ip Adress :{ip}")
    url = f"https://ipinfo.io/{ip}/json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code ==200:
            data = response.json()
            print(Fore.YELLOW+f"🌍 Ip adress : {data.get ('ip','N/A')}")
            print(Fore.YELLOW+f"📍 Location : {data.get ('region','Unknown')},{data.get('countru','Unknown')},{data.get('city','Unknown')}")
            print(Fore.YELLOW+f"🏢 ISP : {data.get ('org','Unknown')}")
            print(Fore.YELLOW+f"🛰️ Coordinated : {data.get('loca','Unknown')}")
    except requests.exceptions.RequestException as e:
        print(Fore.RED+f"Error:{e}")


if __name__ == "__main__":
    main()