def check_age(age):
    if age < 0:
        return "Invalid age entered."
    elif age > 0 and age < 13:
        return "you are a child."
    elif age >= 13 and age < 20:
        if age >= 18:
            return "You are a teenager and also eligible for voting."
        else:
            return "You are a teenager but not eligible for voting."
    elif age >= 20 and age < 59:
        return "You are an adult."
    else:
        return "You are a senior citizen."
    
def main():
    age = int(input("Enter your age: "))
    status = check_age(age)
    print(f"Status based on age: \n{status}")

if __name__ == "__main__":
    main()

