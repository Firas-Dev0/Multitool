import os
import requests


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r'''
    
  _    _ _      _____     _____ _    _  ____  _____ _______ _   _ ______ _____  
 | |  | | |    |  __ \   / ____| |  | |/ __ \|  __ \__   __| \ | |  ____|  __ \ 
 | |  | | |    | |__) | | (___ | |__| | |  | | |__) | | |  |  \| | |__  | |__) |
 | |  | | |    |  _  /   \___ \|  __  | |  | |  _  /  | |  | . ` |  __| |  _  / 
 | |__| | |____| | \ \   ____) | |  | | |__| | | \ \  | |  | |\  | |____| | \ \ 
  \____/|______|_|  \_\ |_____/|_|  |_|\____/|_|  \_\ |_|  |_| \_|______|_|  \_\
                                                                                
                                                                                
[1] Shorten URL [2] exit
    ''')
    option = input("Choose an option: ")

    if option == '1':
        url = input("Enter the URL to shorten: ")
        short_url = shorten_url(url)
        print(f"Shortened URL: {short_url}")
    elif option == '2':
        exit()
    else:
        print("Invalid option. Please try again.")

def shorten_url(url):
    api_url = f"https://tinyurl.com/api-create.php?url={url}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.text
        else:
            return "Failed to shorten URL."
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    main()
    