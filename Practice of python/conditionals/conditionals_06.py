def strength(length):
    if length < 6:
        print("Weak! Password strength")
    elif length < 8:
        print("Medium! Password strength")
    else:
        print("Strong! Password Strength")

def main():
    password = input("Enter your password: ")
    length = len(password)
    strength(length)

if __name__ == "__main__":
    main()

