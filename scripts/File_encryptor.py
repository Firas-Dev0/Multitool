from Crypto.Cipher import AES
import os
import sys
from Crypto.Util.Padding import pad


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r''' 
______ _ _        _____                            _    ______                           _   
|  ___(_) |      |  ___|                          | |   |  _  \                         | |  
| |_   _| | ___  | |__ _ __   ___ _ __ _   _ _ __ | |_  | | | |___  ___ _ __ _   _ _ __ | |_ 
|  _| | | |/ _ \ |  __| '_ \ / __| '__| | | | '_ \| __| | | | / _ \/ __| '__| | | | '_ \| __|
| |   | | |  __/ | |__| | | | (__| |  | |_| | |_) | |_  | |/ /  __/ (__| |  | |_| | |_) | |_ 
\_|   |_|_|\___| \____/_| |_|\___|_|   \__, | .__/ \__| |___/ \___|\___|_|   \__, | .__/ \__|
                                        __/ | |                               __/ | |        
                                       |___/|_|                              |___/|_|        
[1]  Encrypt               [2]  Decrypt
    ''')

    option = input("Choose an option: ")

    if option == '1':
        file_encryptor()
    elif option == '2':
        file_decryptor()
    else:
        print("Invalid option. Please try again.")
        sys.exit(1)
          
def file_encryptor():
    input_file = input("Enter the path of the file to encrypt: ")
    output_file = input("Enter the path to save the encrypted file (default local directory): ")
    if not output_file:
        output_file = os.path.join(os.getcwd(), os.path.basename(input_file) + ".enc")
    key = os.urandom(32)  # AES key size must be either 16, 24, or 32 bytes
    iv = os.urandom(16)  # AES block size is 16 bytes
    
    with open(input_file, 'rb') as f:
        data = f.read()
    padded_data = pad(data, AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(padded_data)
    with open(output_file, 'wb') as f:
        f.write(iv + encrypted_data)

        print(f"File encrypted successfully. Key: {key.hex()}")
        print(f"iv (hex): {iv.hex()}")
        print(f"Encrypted file saved to: {output_file}")

def file_decryptor():
    input_file = input("Enter the path of the file to decrypt: ")
    output_file = input("Enter the path to save the decrypted file (press enter for default local directory): ")
    if not output_file:
        output_file = os.path.join(os.getcwd(), os.path.basename(input_file)[:-4])
    key = bytes.fromhex(input("Enter the encryption key (hex): "))
    
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        encrypted_data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    
    with open(output_file, 'wb') as f:
        f.write(decrypted_data.rstrip(b'\0'))

    print(f"File decrypted successfully. Decrypted file saved to: {output_file}")


if __name__ == "__main__":
    main()