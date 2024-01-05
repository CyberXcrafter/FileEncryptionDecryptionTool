#pip install cryptography

from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_path + '.enc', 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_path[:-4], 'wb') as f:
        f.write(decrypted_data)

# Generate a key
key = generate_key()
print("Generated Key:", key.decode())

# Replace 'file_to_encrypt.txt' with the path to your file
file_path = 'file_to_encrypt.txt'

# Encrypt the file
encrypt_file(file_path, key)

# Decrypt the file
#decrypt_file(file_path + '.enc', key)
