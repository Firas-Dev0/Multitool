import random
import os
from colorama import Fore 
import sys

if sys.platform == "win32":
    import ctypes
    ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(Fore.CYAN + r'''

______                                   _                                   _             
| ___ \                                 | |                                 | |            
| |_/ /_ _ ___ _____      _____  _ __ __| |   __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
|  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` |  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| | | (_| \__ \__ \\ V  V / (_) | | | (_| | | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                              __/ |                                        
                                             |___/                                         
                                                                                                                                                                                                                               
                                                                                                                                                                                                                                          
[1] Generate Password 8 letters [2] Generate Password 12 letters [3] Generate Password 16 letters
[4] Generate Password 20 letters [5] Generate Password 24 letters [6] Generate Password 32 letters

    ''')
    option = input("Choose an option: ")

    length_map = {
        '1': 8,
        '2': 12,
        '3': 16,
        '4': 20,
        '5': 24,
        '6': 32,
    }

    if option in length_map:
        length = length_map[option]
        password = generate_password(length)
        print(Fore.GREEN + f"Generated password: {password}")
    else:
        print(Fore.RED + "Invalid option. Please try again.")
        main()

def generate_password(length):
    chzaracters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    numbers = "0123456789"
    for i in range(length):
        password = ''.join(random.sample(chzaracters, length))
        if any(char in numbers for char in password):
            return password
if __name__ == "__main__":
    main()

