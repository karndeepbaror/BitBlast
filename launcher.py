import sys
from cryptography.fernet import Fernet

def main():
    print("=== BitBlast Launcher ===")
    key_input = input("Enter your decryption key: ").strip()
    key = key_input.encode()

    encrypted_file = "bitblast.enc"

    try:
        with open(encrypted_file, "rb") as file:
            encrypted_data = file.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        exec(decrypted_data.decode())
    except FileNotFoundError:
        print(f"[!] Encrypted file '{encrypted_file}' not found!")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Decryption or execution failed: {e}")
        sys.exit(1)

if _name_ == "_main_":
    main()
