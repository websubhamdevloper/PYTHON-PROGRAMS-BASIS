def func(): #making functions
    print("Hello World")
func() #Calling functions

def oddevenchecker(): #Without any parameters
    num = 2
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
oddevenchecker()

num = 9
def checker(number): # with parameters
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
checker(num)

def fun(x, y=10): #Default argument
    print(x, y)
fun(num)

def student(fname, lname): #using keywords and assigning the values at the moment of calling the functions
    print(f"First Name is {fname} and Last Name is {lname}")

student(fname = "subham", lname = "kundu")

# In Python Arbitrary Keyword Arguments, *args and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:
# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)

def myfunc(*args, **kwargs):
    print("Non-keyword arguments (*args): ")
    for arg in args:
        print(arg)
    print("Keywords arguments (**kwargs): ")
    for key, value in kwargs.items() :
        print(f"{key} == {value}")
    for kwarg in kwargs:
        print(f"{kwargs} == {kwarg}")

myfunc("Hello,", "Welcome", sname = "Subham", lname = "kundu", nickname = "raja")

# A function defined inside another function is called an inner function (or nested function). It can access variables from the enclosing function’s scope and is often used to keep logic protected and organized.


def f1():
    print("function 1")
    fname_f1 = "Raja"
    def f2():
        print("function 2")
        print(fname_f1)
    f2()
f1()

# In Python, an anonymous function means that a function is without a name. As we already
# know the def keyword is used to define the normal
# functions and the lambda keyword is used to create anonymous functions.

lambda_cube = lambda x :x * x * x
print(lambda_cube(num))

def square_num(value):
    return value ** 2
print(square_num(5))
sq_num = square_num(5)
print(sq_num)


def change_element(list_pass): #It can only change the value of List and dictionary (mutable datatypes)
    list_pass[0] = 4

list_original = [5, 9, 8]
print(list_original)
change_element(list_original)
print(list_original)

def factorial(num_fact):
    if num_fact == 0:
        return 1
    else:
        return num_fact * factorial(num_fact -1)

print(factorial(4))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

