from cryptography.fernet import Fernet
key = Fernet.generate_key()

with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('nba.csv', 'rb') as file:
    original = file.read()

encrypted = fernet.encrypt(original)

with open('nba.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

fernet = Fernet(key)

with open('nba.csv', 'rb') as enc_file:
    encrypted = enc_file.read()
decrypted = fernet.decrypt(encrypted)

with open('nba.csv', 'wb') as dec_file:
    dec_file.write(decrypted)