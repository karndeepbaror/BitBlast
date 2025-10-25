
from cryptography.fernet import Fernet
import getpass
import sys
import os

def main():
    enc_file = "bitblast.enc"
    if not os.path.isfile(enc_file):
        print(f"❌ Encrypted file '{enc_file}' नहीं मिली।")
        sys.exit(1)

    try:
        # from user key input (hidden)
        key = getpass.getpass("Enter decryption key: ").encode()

        # Fernet object
        fernet = Fernet(key)

        # Read Encrypted File
        with open(enc_file, "rb") as file:
            encrypted_data = file.read()

        # Decrypt
        decrypted_code = fernet.decrypt(encrypted_data)

        # Run Decrypted Code
        exec(decrypted_code.decode())

    except KeyboardInterrupt:
        print("\n❌ Process cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Decryption failed: {e}")
        sys.exit(1)

if _name_ == "_main_":
    main()
