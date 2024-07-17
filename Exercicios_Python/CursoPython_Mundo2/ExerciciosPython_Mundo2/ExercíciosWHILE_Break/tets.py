from cryptography.fernet import Fernet

# Gerar uma chave de cryp
key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)
