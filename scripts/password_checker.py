import requests
import hashlib
import os
from colorama import Fore

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLUE + r'''
    _____                                    _        _               _             
    |  __ \                                  | |      | |             | |            
    | |__) |_ _ ___ _____      _____  _ __ __| |   ___| |__   ___  ___| | _____ _ __ 
    |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |  / __| '_ \ / _ \/ __| |/ / _ \ '__|
    | |  | (_| \__ \__ \\ V  V / (_) | | | (_| | | (__| | | |  __/ (__|   <  __/ |   
    |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \___|_| |_|\___|\___|_|\_\___|_|   
    ''')
    
    passz = input("Enter the password to check: ").strip()
    if not passz:
        print("No password provided. Exiting.")
        main()

    count = check(passz)
    if count:
        print(f"Warning: Your password has been exposed {count} times in data breaches.")
        print("Consider changing it immediately!")
    else:
        print("Good news: Your password has not been exposed.")

def check(passz):
    sha1 = hashlib.sha1(passz.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        res = requests.get(url)
        res.raise_for_status()
    except requests.RequestException:
        print("Error connecting to the API...")
        return 0

    hashes = (line.split(':') for line in res.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

if __name__ == "__main__":
    main()