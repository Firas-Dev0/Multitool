import os
import subprocess
from colorama import Fore


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r'''
._____________  __________.__                             
|   \______   \ \______   \__| ____    ____   ___________ 
|   ||     ___/  |     ___/  |/    \  / ___\_/ __ \_  __ \
|   ||    |      |    |   |  |   |  \/ /_/  >  ___/|  | \/
|___||____|      |____|   |__|___|  /\___  / \___  >__|   
                                  \//_____/      \/       
[1]  Ping 
[2]  Exit
''')
    choice = input("Choose an option: ")
    if choice == '1':
        ping()
    elif choice == '2':
        exit()
    else:
        print("Invalid option. Please try again.")
        main()
def ping():
    Ip_adress = input(Fore.RED +"Ip adress to ping :")
    numerics = "123456789."
    is_number = True
    for i in Ip_adress :
        if i not in numerics:
            is_number = False
            print("Valeur saisie invalide...")
            return
    if is_number:
        subprocess.run(f"ping -t {Ip_adress}")
    
if __name__ == "__main__":
    main()
