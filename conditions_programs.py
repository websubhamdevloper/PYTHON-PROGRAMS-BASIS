number = 2
check_number = 4
if number > 0:
    print(f"Number is positive : {number}")
else:
    print(f"Number is negative : {number}")

name = "subham"
if name == "subham" or name == "Subham":
    print("true")
else:
    print("false")

_name = "SUBHAM"
if _name.lower() == "subham":
    print("Name is", _name.lower())
else:
    print("Name is not subham")

name_ = "subham"
if name_.upper() == "SUBHAM":
    print("Name is", name.upper())
else:
    print("Name is not SUBHAM")


list_values = [2, 5, 6, 10]
if list_values[0] > list_values[1]:
    print(f"List value in index 0 is greater than the index at 1 : {list_values[0]} & {list_values[1]}")
else:
    print(f"Vice Versa")

if number in list_values:
    print(f"Number {number} is in the list")
else:
    print(f"Number {number} is not in the list")

if check_number not in list_values:
    print(f"Check {check_number} is not in the list")
else:
    print(f"Check {check_number} is in the list")

age = 18 #Below code s ternary operator
vote_eligibility = "Eligible" if age >= 18 else "Not eligible" #shorthand if-else statement for single-line checks
print(f"Eligibility status : {vote_eligibility}")

child_age = 12

if child_age <= 10:
    print(f"Child can travel for free : {child_age}")
elif 11 <= child_age <= 15: #It can be written as -> elif child_age >= 11 and child_age <= 15:
    print(f"child can travel at half-ticket price : {child_age}")
else:
    print(f"Child needs to pay full ticket price : {child_age}")

match number:
    case 1 :
        print("Number does not match")
    case 2:
        print("Number matches")
    case _:
        print("Out of range")
