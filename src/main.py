from fernetKey import generateKey, loadKey
from password import Password
from passwordServices import loadPasswords, addPassword, showPasswords, showServices, saveAllPasswords

globalPasswords = list[Password]()


def main():
    choice = input("Do you already have a secret key? (y/n):").strip().lower()
    if choice == "y":
        print("Select the file secret.key")
    elif choice == "n":
        generateKey()
        print("Key generated successfully\nNow select the file secret.key")
    else:
        return
    key = loadKey()

    global globalPasswords
    globalPasswords = loadPasswords(key)

    while True:
        print("1. Add a new password")
        print("2. Show all passwords")
        print("3. Delete a password")
        choice = input("Enter your choice:").strip()
        if choice == "1":
            addPassword(globalPasswords, key)
        elif choice == "2":
            print(showPasswords(globalPasswords))
        elif choice == "3":
            print("Select the password to delete:")
            print(showServices(globalPasswords))
            index = int(input("Enter the index of password to delete:"))
            if 1 <= index <= len(globalPasswords):
                globalPasswords.pop(index - 1)
                saveAllPasswords(globalPasswords, key)
            else:
                print("Invalid index")
        else:
            return


main()
