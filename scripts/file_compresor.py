import requests
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r'''
___________.__.__                                                                                
\_   _____/|__|  |   ____     ____  ____   _____ _____________   ____   ______ _________________ 
 |    __)  |  |  | _/ __ \  _/ ___\/  _ \ /     \\____ \_  __ \_/ __ \ /  ___//  ___/  _ \_  __ \
 |     \   |  |  |_\  ___/  \  \__(  <_> )  Y Y  \  |_> >  | \/\  ___/ \___ \ \___ (  <_> )  | \/
 \___  /   |__|____/\___  >  \___  >____/|__|_|  /   __/|__|    \___  >____  >____  >____/|__|   
     \/                 \/       \/            \/|__|               \/     \/     \/             
[1]  Compress File            [2]  Decompress File
    ''')
    choice = input("Choose an option: ")
    if choice == '1':
        compress_file()
    elif choice == '2':
        decompress_file()
    else:
        print("Invalid option. Please try again.")
        main()
def compress_file():
    os.system('cls' if os.name == 'nt' else 'clear')
    file_path = input("Enter the path of the file to compress: ")
    if not os.path.isfile(file_path):
        print("File not found. Please check the path and try again.")
        return
    compressed_file_path = file_path + ".zip"
    with open(file_path, 'rb') as f_in:
        with open(compressed_file_path, 'wb') as f_out:
            f_out.write(f_in.read())
    print(f"File compressed successfully: {compressed_file_path}")

def decompress_file():
    os.system('cls' if os.name == 'nt' else 'clear')
    file_path = input("Enter the path of the file to decompress: ")
    if not os.path.isfile(file_path):
        print("File not found. Please check the path and try again.")
        return
    decompressed_file_path = file_path.replace(".zip", "")
    with open(file_path, 'rb') as f_in:
        with open(decompressed_file_path, 'wb') as f_out:
            f_out.write(f_in.read())
    print(f"File decompressed successfully: {decompressed_file_path}")

if __name__ == "__main__":
    main()