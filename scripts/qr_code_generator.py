import pyqrcode
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r'''                                                                                                
 _____ _____    _____ _____ ____  _____    _____ _____ _____ _____ _____ _____ _____ _____ _____ 
|     | __  |  |     |     |    \|   __|  |   __|   __|   | |   __| __  |  _  |_   _|     | __  |
|  |  |    -|  |   --|  |  |  |  |   __|  |  |  |   __| | | |   __|    -|     | | | |  |  |    -|
|__  _|__|__|  |_____|_____|____/|_____|  |_____|_____|_|___|_____|__|__|__|__| |_| |_____|__|__|
   |__|                                                                                          

    ''')
    url_input = input("Enter the URL to generate a QR code: ").strip()
    if not url_input:
        print("No URL provided. Exiting.")
        return

    # Generate QR code
    qr = pyqrcode.create(url_input)

    # Display QR code in terminal
    print("\nHere is your QR code:\n")
    print(qr.terminal(quiet_zone=1))

    # Save QR code as PNG
    qr.png("qrcode.png", scale=6)
    print("\nQR code saved as 'qrcode.png'.")

if __name__ == "__main__":
    main()