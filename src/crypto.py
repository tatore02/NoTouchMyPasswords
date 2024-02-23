from cryptography.fernet import Fernet
from fernetKey import loadKey
from password import Password
import pickle

FILE_NAME = "passwords.dat"
key = None


def readEncryptedPasswordsFromFile() -> list[Password]:
    passwords = list[Password]()
    with open(FILE_NAME, "rb") as file:
        while True:
            encryptedData = file.readline()
            if not encryptedData:
                break
            passwords.append(decryptPassword(encryptedData))
    return passwords


def appendEncryptedPasswordToFile(passwords: list[Password]()):
    with open(FILE_NAME, "wb") as file:
        for password in passwords:
            file.write(encryptPassword(password) + b"\n")


def encryptPassword(password: Password):
    _checkKey()
    f = Fernet(key)
    serializedPassword = pickle.dumps(password)
    return f.encrypt(serializedPassword)


def decryptPassword(encryptedData):
    _checkKey()
    f = Fernet(key)
    decrypted_data = f.decrypt(encryptedData)
    return pickle.loads(decrypted_data)


def _checkKey():
    global key
    if key is None:
        key = loadKey()
