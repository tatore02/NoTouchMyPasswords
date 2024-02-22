from cryptography.fernet import Fernet
from password import Password
import pickle

FILE_NAME = "passwords.dat"


def readEncryptedPasswordsFromFile(key: bytes) -> list[Password]:
    passwords = list[Password]()
    with open(FILE_NAME, "rb") as file:
        while True:
            encryptedData = file.readline()
            if not encryptedData:
                break
            passwords.append(decryptPassword(encryptedData, key))
    return passwords


def appendEncryptedPasswordToFile(passwords: list[Password](), key: bytes):
    with open(FILE_NAME, "wb") as file:
        for password in passwords:
            file.write(encryptPassword(password, key))
            file.write(b"\n")


def encryptPassword(password: Password, key: bytes):
    f = Fernet(key)
    serializedPassword = pickle.dumps(password)
    return f.encrypt(serializedPassword)


def decryptPassword(encryptedData, key: bytes):
    f = Fernet(key)
    decrypted_data = f.decrypt(encryptedData)
    return pickle.loads(decrypted_data)
