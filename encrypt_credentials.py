import base64
import json
import os
import sys
import hashlib
from cryptography.fernet import Fernet

def encrypt_credentials():
    """Encrypt the Firebase credentials file and save the encrypted string."""
    credentials_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'credentials.json')
    
    if not os.path.exists(credentials_path):
        print(f"Error: credentials.json not found at {credentials_path}")
        print("Please make sure credentials.json is in the same directory as this script.")
        return
    
    print(f"Found credentials file at: {credentials_path}")
    
    # Read the credentials file
    try:
        with open(credentials_path, 'r') as file:
            creds_data = file.read()
        
        # Validate that it's proper JSON
        json.loads(creds_data)
    except json.JSONDecodeError:
        print("Error: credentials.json is not a valid JSON file.")
        return
    except Exception as e:
        print(f"Error reading credentials file: {str(e)}")
        return
    
    try:
        # Generate the encryption key (same method as in the main app)
        machine_id = os.name + sys.platform
        key_material = machine_id.encode() + b'hangman_secure_key'
        key_hash = hashlib.sha256(key_material).digest()
        key = base64.urlsafe_b64encode(key_hash[:32])
        
        # Encrypt the credentials
        cipher = Fernet(key)
        encrypted_data = cipher.encrypt(creds_data.encode())
        
        # Save the encrypted string to a file
        output_file = 'encrypted_credentials.txt'
        with open(output_file, "wb") as f:
            f.write(encrypted_data)
        
        print(f"\n✅ Successfully encrypted credentials to {output_file}")
        
        # Test decryption to verify it works
        try:
            with open(output_file, 'rb') as f:
                read_data = f.read()
            
            decrypted = cipher.decrypt(read_data)
            json.loads(decrypted)
            print("✅ Successfully verified encryption/decryption!")
        except Exception as e:
            print(f"❌ Warning: Decryption verification failed: {str(e)}")
        
        # Print instructions for developers
        print("\n=== INSTRUCTIONS ===")
        print("For development:")
        print("  1. The file 'encrypted_credentials.txt' has been created")
        print("  2. Keep this file in the same directory as hangman.py")
        print("  3. The app will now automatically load credentials from this file")
        
        print("\nFor distribution:")
        print("  1. Use this PyInstaller command:")
        print("     pyinstaller --windowed --name=\"Hangman\" --add-data=\"images:images\" --add-data=\"encrypted_credentials.txt:.\" hangman.py")
        print("  2. This will include the encrypted credentials in your bundled app")
            
    except Exception as e:
        print(f"Error during encryption: {str(e)}")

if __name__ == "__main__":
    encrypt_credentials()
