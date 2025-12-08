#Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

mytuple = (1, 5, 9)
print(mytuple)

length_tuple = len(mytuple) #length of the tuple using len() method
print(length_tuple)

single_tuple = ("apple",) #For single item tuple, we have to use comma after the value/element
print(single_tuple)

converting_tuple = tuple(("apple", "banana")) #Converting a datatype into tuple using tuple() method
print(converting_tuple)

#Accessing the items/values/elements in the tuple
print(mytuple[1])

print(mytuple[-1]) #returns the last element of  the tuple

print(mytuple[0:2]) #using range (in python "slice") method


#checking whether an element exists in the tuple or not
sample_tuple = ("apple", "banana", "orange", "kiwi")
if "kiwi" in sample_tuple:
    print(f"Kiwi is in {sample_tuple}")

#Manipulating the elements of the tuple by converting the tuple into list then converting it back to tuple
con_tuple = (1, 8, 0)
print(con_tuple)
temp_list = list(con_tuple)
temp_list[2] = 2
con_tuple = tuple(temp_list)
print(con_tuple)

#adding a new tuple to an exiting tuple
existing_tuple = ("apple", "banana")
print(existing_tuple)
add_tuple = ("kiwi", "orange")
print(add_tuple)
existing_tuple += add_tuple
print(existing_tuple)

#Deleting a tuple using del keyword
del add_tuple

#packing and unpacking of tuple
fruits_tuple = ("apple", "banana", "orange") #Packing
(red_fruit, yellow_fruit, orange_fruit) = fruits_tuple #Unpacking
print(red_fruit)
print(yellow_fruit)
print(orange_fruit)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits #If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
print(green)
print(yellow)
print(red)

fruits_ = ("apple", "mango", "papaya", "pineapple", "cherry")
(green_, *tropic, red_) = fruits_  #If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
print(green_)
print(tropic)
print(red_)


print("")
#Loops in tuple {For loops}
for items in fruits: #items access the elements of the tuple
    print(items)

print(" ")

for i in range(len(fruits)): #i access the index of the elements in the tuple
    print(fruits[i])

print(" ")

#{While Loops}
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

print(" ")

#joing of two or more tuple
tuple1 = ("apple", "banana")
print(tuple1)
tuple2 = ("kiwi", "grape")
print(tuple2)
tuple3 = tuple1 + tuple2
print(tuple3)

#multipling the elements of the tuple

temp_tuple_test = ("apple", "banana")
mul_tuple = temp_tuple_test * 2
print(mul_tuple)

#counting the element in the tuple {duplicates}
duplicate_value_tuple = (1, 7, 2, 7, 3, 8, 7)
count_element = duplicate_value_tuple.count(7)
print(count_element)

#index of any value in the tuple
tuple_index = (2, 9, 6)
value_loc = tuple_index.index(9)
print(value_loc)

