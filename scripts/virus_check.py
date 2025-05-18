import requests
import json
import time
import os
from colorama import Fore

API_KEY = '8bd0f8c91b175b44e5ffcc9c5849c34c6cd0747ba7925c65fa2786241cab991b'
HEADERS = {'x-apikey': API_KEY}

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLUE + r'''

                                                                 ,----..    ,---,                              ,-.
       ,---.  ,--,                                              /   /   \ ,--.' |                          ,--/ /|
      /__./|,--.'|    __  ,-.         ,--,                     |   :     :|  |  :                        ,--. :/ |
 ,---.;  ; ||  |,   ,' ,'/ /|       ,'_ /|   .--.--.           .   |  ;. /:  :  :                        :  : ' /
/___/ \  | |`--'_   '  | |' |  .--. |  | :  /  /    '          .   ; /--` :  |  |,--.   ,---.     ,---.  |  '  /
\   ;  \ ' |,' ,'|  |  |   ,','_ /| :  . | |  :  /`./          ;   | ;    |  :  '   |  /     \   /     \ '  |  :
 \   \  \: |'  | |  '  :  /  |  ' | |  . . |  :  ;_            |   : |    |  |   /' : /    /  | /    / ' |  |   \
  ;   \  ' .|  | :  |  | '   |  | ' |  | |  \  \    `.         .   | '___ '  :  | | |.    ' / |.    ' /  '  : |. \
   \   \   ''  : |__;  : |   :  | : ;  ; |   `----.   \        '   ; : .'||  |  ' | :'   ;   /|'   ; :__ |  | ' \ \
    \   `  ;|  | '.'|  , ;   '  :  `--'   \ /  /`--'  /        '   | '/  :|  :  :_:,''   |  / |'   | '.'|'  : |--'
     :   \ |;  :    ;---'    :  ,      .-./'--'.     /         |   :    / |  | ,'    |   :    ||   :    :;  |,'
      '---" |  ,   /          `--`----'      `--'---'           \   \ .'  `--''       \   \  /  \   \  / '--'
             ---`-'                                              `---`                 `----'    `----'
''')

def scan_file(file_path):
    url_upload = "https://www.virustotal.com/api/v3/files"
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            resp = requests.post(url_upload, headers=HEADERS, files=files)
    except FileNotFoundError:
        print("File not found. Please check the path.")
        return
    
    if resp.status_code != 200:
        print(f"Error uploading file: {resp.status_code}")
        print("Response:", resp.text)
        return
    
    try:
        data = resp.json()
        analysis_id = data['data']['id']
        analysis_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
    except KeyError:
        print("Error parsing upload response:", resp.text)
        return

    print("\n[*] Waiting for scan to complete...")

    while True:
        resp = requests.get(analysis_url, headers=HEADERS)
        if resp.status_code != 200:
            print(f"Error fetching results: {resp.status_code}")
            print("Response:", resp.text)
            break
        
        result = resp.json()
        status = result.get('data', {}).get('attributes', {}).get('status', 'unknown')
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.BLUE + r'''
                                                                 ,----..    ,---,                              ,-.
       ,---.  ,--,                                              /   /   \ ,--.' |                          ,--/ /|
      /__./|,--.'|    __  ,-.         ,--,                     |   :     :|  |  :                        ,--. :/ |
 ,---.;  ; ||  |,   ,' ,'/ /|       ,'_ /|   .--.--.           .   |  ;. /:  :  :                        :  : ' /
/___/ \  | |`--'_   '  | |' |  .--. |  | :  /  /    '          .   ; /--` :  |  |,--.   ,---.     ,---.  |  '  /
\   ;  \ ' |,' ,'|  |  |   ,','_ /| :  . | |  :  /`./          ;   | ;    |  :  '   |  /     \   /     \ '  |  :
 \   \  \: |'  | |  '  :  /  |  ' | |  . . |  :  ;_            |   : |    |  |   /' : /    /  | /    / ' |  |   \
  ;   \  ' .|  | :  |  | '   |  | ' |  | |  \  \    `.         .   | '___ '  :  | | |.    ' / |.    ' /  '  : |. \
   \   \   ''  : |__;  : |   :  | : ;  ; |   `----.   \        '   ; : .'||  |  ' | :'   ;   /|'   ; :__ |  | ' \ \
    \   `  ;|  | '.'|  , ;   '  :  `--'   \ /  /`--'  /        '   | '/  :|  :  :_:,''   |  / |'   | '.'|'  : |--'
     :   \ |;  :    ;---'    :  ,      .-./'--'.     /         |   :    / |  | ,'    |   :    ||   :    :;  |,'
      '---" |  ,   /          `--`----'      `--'---'           \   \ .'  `--''       \   \  /  \   \  / '--'
             ---`-'                                              `---`                 `----'    `----'

''')
        print(f"Scan status: {status}")

        if status == 'completed':
            print("\n[+] Scan completed. Results:\n")
            print(json.dumps(result, indent=4))
            break
        
        time.sleep(5)

def main():
    print_banner()
    file_path = input("Enter the file path to scan: ").strip()
    if not file_path:
        print("No file provided. Exiting.")
        return
    scan_file(file_path)
    input("\nPress Enter to exit...")

if __name__ == '__main__':
    main()
