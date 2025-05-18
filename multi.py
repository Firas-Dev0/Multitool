import os
import sys
from colorama import Fore
import urllib


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + r'''
 __  __ _    _ _   _______ _____ _______ ____   ____  _      
|  \/  | |  | | | |__   __|_   _|__   __/ __ \ / __ \| |     
| \  / | |  | | |    | |    | |    | | | |  | | |  | | |     
| |\/| | |  | | |    | |    | |    | | | |  | | |  | | |     
| |  | | |__| | |____| |   _| |_   | | | |__| | |__| | |____ 
|_|  |_|\____/|______|_|  |_____|  |_|  \____/ \____/|______|

[1]  Virus Checker                   -        [2]  IP Lookup
[3]  IP Pinger                       -        [4]  Password leak_Checker
[5]  SMS Sender                      -        [6]  QR Code Generator
[7]  URL Shortener                   -        [8]  Password Generator
[9] Password Strength Checker        -        [10] File Encryptor/decryptor
[11] File Compressor/decompressor    -        [12] File Converter
[13] My GitHub Repository
    ''')

    option = input("Choose an option: ")

    if option == '1':
        from scripts.virus_check import main
        main()
    elif option == '2':
        from scripts.IP_Lookup import main
        main()
    elif option == '3':
        from scripts.Ip_pinger import main
        main()
    elif option == '4':
        from scripts.password_checker import main
        main()
    elif option == '5':
        from scripts.Anon_sms import main
        main()
    elif option == '6':
        from scripts.qr_code_generator import qr_code_generator
        qr_code_generator()
    elif option == '7':
        from scripts.url_shortener import main
        main()
    elif option == '8':
        from scripts.password_generator import main
        main()
    elif option == '9':
        from scripts.password_strengh import main
        main()  
    elif option == '10':
        from scripts.File_encryptor import main
        main()
    elif option == '11':
        from scripts.file_compresor import main
        main()
    elif option == '12':
        from scripts.file_convertor import main
        main()
    elif option == '13':
        return urllib.request.urlopen("https://github.com/Firas-Dev0?tab=repositories")
    else:
        print("Invalid option. Please try again.")

# Optional: run if executed directly
if __name__ == '__main__':
    main()
