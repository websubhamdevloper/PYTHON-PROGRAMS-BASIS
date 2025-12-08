list_values = [1, 8, 4, 9]
print(list_values)

for values in list_values: #Accessing the elements of the list
    print(values)

list_name = ["Subham", "Raja", "Viraj"]
print(list_name)
list_name.append("Abir") # Adding a new element at the end of the list

copy_listname = list_name.copy() #Copies the list to the variable
print(copy_listname)

count_element = list_name.count("Subham") #Counts the same element present in the list
print(count_element)

list_extend = ["Ajay", "Birbal", "Kinjal", "Joydwip"]
list_extend.extend(list_name) #Adds a different list to the end of the another list
print(list_extend)

loc_element = list_extend.index("Subham") #Gives the index or location of the element in the list
print(loc_element)

list_extend.pop(1) #Removes the element present at the given index to the pop() method of the list
print(list_extend)

list_extend.remove("Ajay") #removes the element which comes first in the list with same string provided to the method remove()
print(list_extend)

list_name.reverse() #Reverses the list
print(list_name)


list_name.sort() #Sorts the list either alphabetically or numerically
print(list_name)

list_extend.clear() #clear() method removes all the elements in the list
print(f"{list_extend} is empty")

list_length = len(list_name) #Provides the length of the list
print(list_length)

new_list = list((23, 65, 9)) #Using list() method for converting a tuple into a list... list() is a constructor
print(new_list)

#Inserting elements into a list using the inputs of the user
list_user = []
for value in range(5):
    value_user = input(f"Enter the value for list index : {value} :-> ")
    list_user.append(value_user)

print(list_user)
print(len(list_user))


#without List comprehension

fruits = ["apple", "banana", "cherry", "avocado"]
newfruit = []
for fruit in fruits:
    if "a" in fruit:
        newfruit.append(fruit)
    else:
        print(f"Fruits are {fruit}")

print(newfruit)

#with List comprehension

#newlist = [expression for item in iterable if condition == True]

newlist_fruit_comprehension = [x for x in fruits if "a" in x] #Adds element in the list with "a"
print(newlist_fruit_comprehension)

newlist_comprehension = [x for x in fruits if x != "apple"] #Adds elements in the list without apple
print(newlist_comprehension)

only_apple_list = [x for x in fruits if x == "apple"] #Add element in list only apple
print(only_apple_list)

iterable_list = [x for x in range(10)] #Adds 0 to 9 in the list
print(iterable_list)

iterable_conditions = [x for x in range(10) if x < 5] # Adds 0 to given condition range
print(iterable_conditions)

upper_list = [x.upper() for x in list_name] #change all the elements into upper case
print(upper_list)

list_temp = ["Hello", "Hello"]
print(list_temp)
set_element_list = ["Hi" for x in list_temp] #changes all the elements of the list
print(set_element_list)

_templist = [x if x != "banana" else "orange" for x in fruits] #Return the item if it is not banana, if it is banana return orange
print(_templist)

#Important functions / method on sorting in the list

name = ["subham", "shayan", "sukanta", "sagnik", "aditya", "sayan", "suprotik"]
name.sort() #sorts in ascending order
print(name)

des_name = ["subham", "shayan", "sukanta", "sagnik", "aditya", "sayan", "suprotik"]
des_name.sort(reverse=True)
print(des_name)

#Case-sensitive sort() method -> Default in nature

c_name = ["Subham", "aditya", "Bipan", "Sayan", "utpal"]
c_name.sort()
print(c_name)

#Case Insensitive sort() Method

insen_name = ["Subham", "aditya", "Bipan", "Sayan", "utpal"]
insen_name.sort(key = str.lower)
print(insen_name)

#Copying methods of list

copy1_name = list_name.copy()
copy2_name = list(list_name)
copy3_name = list_name[:]
print(copy1_name)
print(copy2_name)
print(copy3_name)


#joining of Lists

list1 = [1, 5, 6]
list2 = [2, 4, 9]
list3 = list1 + list2
print(list3)

#Joining of list using {for loop}
list4 = []
for x in list2:
    list4.append(x)
print(list4)

