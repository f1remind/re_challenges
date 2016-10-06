def check(z):
    a = 0
    for b in range(len(z)):
        a += ord(z[b])*b
    return a==13688

def main():
    password = input("Please enter the passphrase: ")
    login = check(password)
    if login:
        print("Password accepted, welcome!")
    else:
        print("Wrong password!")
    return


'''Standard code to start the main function if the module
has been started directly and not just imported'''
if __name__ == '__main__':
    main()
