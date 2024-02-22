import os
from password import Password
from crypto import appendEncryptedPasswordToFile, readEncryptedPasswordsFromFile

FILE_NAME = "passwords.dat"


def loadPasswords(key) -> list[Password]:
    if not os.path.exists(FILE_NAME):
        return list[Password]()
    return readEncryptedPasswordsFromFile(key)


def savePassword(password: Password, key) -> None:
    pass


def saveAllPasswords(passwords: list[Password], key) -> None:
    appendEncryptedPasswordToFile(passwords, key)


def addPassword(passwords, key) -> list[Password]:
    print("Adding a new password:")
    service = input("Service:").strip()
    username = input("Username:").strip()
    password = input("Password:").strip()
    passwords.append(Password(service, username, password))
    saveAllPasswords(passwords, key)
    # savePassword(Password(service, username, password), key)
    return loadPasswords(key)


def showPasswords(passwords: list[Password]) -> str:
    s = ""
    for password in passwords:
        s += str(password)
        s += "\n"
        s += "-" * 20
        s += "\n"
    return s


def showServices(passwords: list[Password]) -> str:
    s = ""
    i = 0
    for password in passwords:
        s += f"{i}. {password.service}\n"
        i += 1
    return s
