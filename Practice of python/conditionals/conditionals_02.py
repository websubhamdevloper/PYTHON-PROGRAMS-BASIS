def movie_ticket(age, day):
    if age < 0:
        return "Invalid age entered!"
    elif age > 0 and age < 18:
        t_price = 8
        if day.lower() == "wednesday":
            t_price = t_price - 2
        else:
            t_price = t_price
        return f"Ticket price for children is ${t_price}."
    elif age >= 18:
        t_price = 12
        if day.lower() == "wednesday":
            t_price = t_price - 2
        else:
            t_price = t_price 
        return f"Ticket price for adults is ${t_price}."
    else:
        return "Invalid age Entered!"
    
def main():
    age = int(input("Enter your age : "))
    day = input("Enter the day of the week : ")
    print(movie_ticket(age, day))

if __name__ == "__main__":
    main()


