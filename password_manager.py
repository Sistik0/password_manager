from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")

def write_key():
    key = Fernet.generate_key()
    #wb = write in bytes
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            account, passw = data.split("|")
            print("Account: " + account + "| Password: " + fer.decrypt(passw.encode()).decode())

def add():
    name  = input("Account Name: ")
    pwd = input("Password: ")

    #with allows automatic closing of the file, a = append(adds to end or create if file doesn't exist), w = write(clears and overwrites), r = read), 
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones or quit (view/add/q) quit?").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        break
    else:
        print("Invalid mode. Please try again.")
        continue
