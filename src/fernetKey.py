from cryptography.fernet import Fernet

FILE_PATH = ""


def generateKey() -> None:
    key = Fernet.generate_key()
    with open("secret.key", "wb") as keyFile:
        keyFile.write(key)


def loadKey() -> bytes:
    with open(FILE_PATH, "rb") as keyFile:
        key = keyFile.read()
    return key


def setFilePath(filePath: str) -> None:
    global FILE_PATH
    FILE_PATH = filePath
