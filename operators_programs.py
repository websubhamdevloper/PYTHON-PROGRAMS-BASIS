a = 5;   '''We will use these variables 'a' &  'b' in operators'''
b = 10;   '''We will use these variables 'a' &  'b' in operators'''
c = 20

'''Sum / Addition'''
summation_two_variables = a + b
print(f"Addition of two variables value is : {summation_two_variables}")
addition_three_variables = a + b + c
print(f"Addition of three variables is : {addition_three_variables}")

'''subtraction of two variable's values'''
subtraction_two_variables = a - b
sub_of_otherVariables = a - c
print(f"Subtraction of two variables are : {subtraction_two_variables} & {sub_of_otherVariables}")

'''Multiplication'''
multiple = a * b * c
print(f"Multiplication of variable's values is : {multiple}")

'''division of values of two variables'''
div = a / b
print(f"Division of variable's values is : {div}")

'''Floor division'''
floor = a // 8
print(f"Floor division of variable's values is : {floor}")

'''Modulo'''
modulas = a % b
print(f"Modulo of variable's values is : {modulas}")

'''Assignment operator'''
a +=b
print(f"Value of a is : {a}")
a -=b
print(f"Value of a is : {a}")
a *=b
print(f"Value of a is : {a}")
a /=b
print(f"Value of a is : {a}")
a //=b
print(f"Value of a is : {a}")
a **=b
print(f"Value of a is : {a}")
a %=b
print(f"Value of a is : {a}")

print(a is c) # 'is' and 'is not' keywords are used to see if the values inside the two variables are same or not and vice versa
print(a is not c)




