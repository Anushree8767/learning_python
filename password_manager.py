master_pwd = input("What is the master password? ")


def view():
    with open('passwords.txt', 'r')  as f:
        for line in f.readlines():
            print(line)


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a')  as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. ")
        continue