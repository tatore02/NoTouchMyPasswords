from fernetKey import generateKey
from password import Password
from passwordServices import addPassword, getServices, deletePassword, getPassword, editPassword
from utils import printListWithIndex


def main():
    choice = input("Do you already have a secret key? (y/n):").strip().lower()
    if choice == "y":
        print("Select the file secret.key")
    elif choice == "n":
        generateKey()
        print("Key generated successfully\nNow select the file secret.key")
    else:
        return

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
            indexToShow = chooseService()
            if indexToShow is not None:
                print(getPassword(indexToShow))
        elif choice == "3":
            password = insertNewPassword()
            addPassword(password)
        elif choice == "4":
            print("Select the password to edit:")
            indexToEdit = chooseService()
            if indexToEdit is not None:
                editPassword(indexToEdit, insertNewPassword())
        elif choice == "5":
            print("Select the password to delete:")
            indexToDelete = chooseService()
            if indexToDelete is not None:
                deletePassword(indexToDelete)
        else:
            return


def insertNewPassword() -> Password:
    service = input("Service:").strip()
    username = input("Username:").strip()
    password = input("Password:").strip()
    return Password(service, username, password)


def chooseService() -> int | None:
    services = getServices()
    printListWithIndex(services)
    index = int(input("Enter the index:"))
    if 0 <= index < len(services):
        return index
    else:
        print("Invalid index")
        return None


main()
