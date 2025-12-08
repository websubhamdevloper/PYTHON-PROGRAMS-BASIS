name = "subham kundu" #string value
number = 10 #integer value
floating_decimal_number = 10.5 #Decimal/float/double value
boolean_value = True #Boolean value, it can be True and False
character_value = 'c' #Character value
list_value = [1, 3, 4] #List same as Array in Java : Mutable value
dictionary_value = {'a': 1, 'b': 2, 'c': 3, 'd': 4} #Dictionary value {Combination of Key:Value pair}
tuple_value = (1, 5, 7) #Tuple value : Immutable value

num1 = num2 = num3 = 20 #Assigning same value to the multiple variables in the same line
roll_no, age, marks = 96, 21, 89 #Assigning multiple values to multiple variables in the same line

int_value = int(10.5) #typeCasting from Float value to Integer value
float_value = float(10) #Type_casting from integer value to float value
str_value = str(100) #Type_casting from Integer value to String Value but String value to integer or any other number value is impossible

print(type(name)) #"type()" is used to show the data-type of the variable
print(type(number)) #"type()" is used to show the data-type of the variable
print(type(floating_decimal_number)) #"type()" is used to show the data-type of the variable
print(type(boolean_value)) #"type()" is used to show the data-type of the variable
print(type(character_value)) #"type()" is used to show the data-type of the variable
print(type(list_value)) #"type()" is used to show the data-type of the variable
print(type(dictionary_value)) #"type()" is used to show the data-type of the variable
print(type(tuple_value)) #"type()" is used to show the data-type of the variable
print(type(num1)) #"type()" is used to show the data-type of the variable
print(type(num2)) #"type()" is used to show the data-type of the variable
print(type(roll_no)) #"type()" is used to show the data-type of the variable
print(type(int_value)) #"type()" is used to show the data-type of the variable
print(type(float_value)) #"type()" is used to show the data-type of the variable
print(type(str_value)) #"type()" is used to show the data-type of the variable

print(name) #keyword "print()" displays the value present inside the variable
print(number)
print(floating_decimal_number)
print(boolean_value)
print(character_value)
print(list_value)
print(dictionary_value)
print(tuple_value)
print(num1)
print(num2)
print(roll_no)
print(int_value)
print(float_value)
print(str_value)

print(name, number) #displaying multiple variable's value to the monitor

print("Hello, welcome to the world of Python developement") #Directly displaying the value to the screen

print(f"{name} is the name of the user") #{f""} is used when we want to use variable inside the print statement
formatted_display = "Hello, my name is {}".format(name) #using "format()" method to apply variable directly into the assignment of the variable
print(formatted_display)
print("Hello, ", name, "! Welcome to the world of Python developement from the your Java Developement")


#keyword "del" is used to delete a variable from the program from that point of line
# Syntax is "del name", deletes the name variable from the program from that point of line

sentence = input("Please enter a message: ") #keyword "input()" is used to take user-value from the user through terminal
print(sentence)
user_number = int(input("Enter a number: ")) #type-casting the user-input value before assigning to the variable
user_float_value = float(input("Enter a floating value or integer value: ")) #type-casting the user-input value before assigning the value to the variable -> any number to float
print(user_float_value)

input_value1, input_value2 = input("Enter two numbers :").split() #using "split()" method we can take multiple user-input value to multiple variables
print(input_value1)
print(input_value2)





