from fernetKey import generateKey, setFilePath
from password import Password
from passwordServices import fillGlobalPasswords, addPassword, getServices, deletePassword, getPassword, editPassword
from utils import printListWithIndex
from tkinter import filedialog, Tk


def startup(filePath: str) -> None:
    setFilePath(filePath)
    fillGlobalPasswords()


def main():
    tkinterRoot = Tk()
    choice = input("Do you already have a secret key? (y/n):").strip().lower()
    if choice == "y":
        print("Select the file secret.key")
        filePath = filedialog.askopenfilename(title="Select the file secret.key")
    elif choice == "n":
        generateKey()
        filePath = "secret.key"
        print("Key generated successfully\nNow select the file secret.key")
    else:
        return

    startup(filePath)

    while True:
        print("1. Show all services\n" +
              "2. Show a password\n" +
              "3. Add a new password\n" +
              "4. Edit a password\n" +
              "5. Delete a password")
        choice = input("Enter your choice:").strip()
        if choice == "1":
            printListWithIndex(getServices())
        elif choice == "2":
            printListWithIndex(getServices())
            print("Select the password to show:")
            indexToShow = _chooseService()
            if indexToShow is not None:
                print(getPassword(indexToShow))
        elif choice == "3":
            password = _insertNewPassword()
            addPassword(password)
        elif choice == "4":
            print("Select the password to edit:")
            indexToEdit = _chooseService()
            if indexToEdit is not None:
                editPassword(indexToEdit, _insertNewPassword())
        elif choice == "5":
            print("Select the password to delete:")
            indexToDelete = _chooseService()
            if indexToDelete is not None:
                deletePassword(indexToDelete)
        else:
            return


def _insertNewPassword() -> Password:
    service = input("Service:").strip()
    username = input("Username:").strip()
    password = input("Password:").strip()
    return Password(service, username, password)


def _chooseService() -> int | None:
    services = getServices()
    printListWithIndex(services)
    index = int(input("Enter the index:"))
    if 0 <= index < len(services):
        return index
    else:
        print("Invalid index")
        return None


if __name__ == "__main__":
    window = Tk()
    window.geometry("600x600")
    window.title("Hello TkInter!")
    window.resizable(False, False)
    window.configure(background="white")
