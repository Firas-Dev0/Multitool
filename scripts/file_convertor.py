import requests
import os
import sys
import convertapi
from zamzar import ZamzarClient


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r'''

  ______ _ _                                      _             
 |  ____(_) |                                    | |            
 | |__   _| | ___    ___ ___  _ ____   _____ _ __| |_ ___  _ __ 
 |  __| | | |/ _ \  / __/ _ \| '_ \ \ / / _ \ '__| __/ _ \| '__|
 | |    | | |  __/ | (_| (_) | | | \ V /  __/ |  | || (_) | |   
 |_|    |_|_|\___|  \___\___/|_| |_|\_/ \___|_|   \__\___/|_|   
                                                                
                                                                
[1] convert.api [2] zamzar [4] exit
print("PLEASE REPLACE THE API SECRET KEY IN THE CODE !!! OR USE THE ZAMZAR OPTION WITH DEFAULT API KEY 100 conversions before you need to change the key")
    ''')
    option = input("Choose an option: ")

    if option == '1':
        convert_file()
    elif option == '4':
        sys.exit()
    elif option == '2':
        zamzar()
    else:
        print("Invalid option. Please try again.")
        main()

def convert_file():
    File = input("Enter the file path you want to convert: ")
    if not os.path.isfile(File):
        print("File not found. Please check the path and try again.")
        return
    extension = input("Enter the file extension you want to convert to (e.g., jpg, png): ")
    if not extension.startswith('.'):
        extension = '.' + extension
    convertapi.api_secret = ''  # Replace with your ConvertAPI secret key
    result = convertapi.convert(extension, {'File': File})
    result.save_files(os.getcwd())  # Replace with your desired output path
    print(f"File converted and saved to {os.getcwd()}")

def zamzar():
    File = input("Enter the file path you want to convert: ")
    if not os.path.isfile(File):
        print("File not found. Please check the path and try again.")
        zamzar()
    Format = input("Enter the file extension you want to convert to (e.g., jpg, png): ")
    if Format.startswith('.'):
        Format = Format[1:] 
    path = os.getcwd()
    try:
        client = ZamzarClient(api_key='145254fe17d9a0785044e1a17fa461d9e262402f') # Replace with your Zamzar API key
        client.convert(File, Format).store(path).delete_all_files()
        print(f"File converted and saved to {path}")
    except Exception as e:
        print(f"An error occurred: {e}")
        zamzar()

if __name__ == "__main__":
    main()