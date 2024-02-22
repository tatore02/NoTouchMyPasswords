from cryptography.fernet import Fernet
from tkinter import filedialog, Tk


def generateKey() -> None:
    key = Fernet.generate_key()
    with open("secret.key", "wb") as keyFile:
        keyFile.write(key)


def loadKey() -> bytes:
    # filePath = filedialog.askopenfilename(title="Select the file secret.key")
    with open("secret.key", "rb") as keyFile:
        key = keyFile.read()
    return key
