from password import Password
from crypto import appendEncryptedPasswordToFile, readEncryptedPasswordsFromFile

globalPasswords = list[Password]()


def fillGlobalPasswords() -> None:
    global globalPasswords
    globalPasswords = readEncryptedPasswordsFromFile()


def saveAllPasswords() -> None:
    appendEncryptedPasswordToFile(globalPasswords)


def addPassword(password: Password) -> None:
    globalPasswords.append(password)
    saveAllPasswords()


def deletePassword(indexPassword: int) -> None:
    globalPasswords.pop(indexPassword)
    saveAllPasswords()


def editPassword(indexPassword: int, newPassword: Password) -> None:
    globalPasswords[indexPassword] = newPassword
    saveAllPasswords()


def getServices() -> list[str]:
    services = []
    for password in globalPasswords:
        services.append(password.service)
    return services


def getPassword(index: int) -> Password | None:
    return globalPasswords[index]
