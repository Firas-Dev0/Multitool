import re
import os
from colorama import Fore


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + r'''
  _____                                    _       _                        _            _               _             
 |  __ \                                  | |     | |                      | |          | |             | |            
 | |__) |_ _ ___ _____      _____  _ __ __| |  ___| |_ _ __ ___ _ __   __ _| |__     ___| |__   ___  ___| | _____ _ __ 
 |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` | / __| __| '__/ _ \ '_ \ / _` | '_ \   / __| '_ \ / _ \/ __| |/ / _ \ '__|
 | |  | (_| \__ \__ \\ V  V / (_) | | | (_| | \__ \ |_| | |  __/ | | | (_| | | | | | (__| | | |  __/ (__|   <  __/ |   
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_| |___/\__|_|  \___|_| |_|\__, |_| |_|  \___|_| |_|\___|\___|_|\_\___|_|   
                                                                       __/ |                                           
                                                                      |___/                                            
    ''')
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)
def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase and lowercase check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")

    # Digit check
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include at least one digit.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*, etc.).")

    # Strength score evaluation
    if strength == 4:
        return "Strong password ✅"
    elif strength == 3:
        return "Moderate password ⚠️\n" + "\n".join(feedback)
    else:
        return "Weak password ❌\n" + "\n".join(feedback)

if __name__ == "__main__":
    main()
