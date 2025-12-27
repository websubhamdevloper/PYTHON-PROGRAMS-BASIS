def coffee_size(order, expresso):
    if order == "small":
        order_list =  "You ordered a small coffee."
        if expresso == True or expresso == "yes" or expresso == "y":
            order_list += " An extra shot of expresso."
            return order_list
        else:
            return order_list
    elif order == "medium":
        order_list = "You ordered a medium coffee."
        if expresso == True or expresso == "yes" or expresso == "y":
            order_list += " An extra shot of expresso."
            return order_list
        else:
            return order_list
    elif order == "large":
        order_list = " You have ordered a large coffee."
        if expresso == True or expresso == "yes" or expresso == "y":
            order_list += " An extra shot of expresso."
            return order_list
        else:
            return order_list
    else:
        return "Invalid Size of the coffee."
    
def main():
    order = input("Enter the size of the coffee {Small, Medium, Large} : ").lower()
    expresso = input("Do you need extra Expresso {Yes, y or No, n} : ").lower()
    coffee = coffee_size(order, expresso)
    print(f"Your Order list:\n{coffee}")

if __name__ == "__main__":
    main()

