dict_ = {                #Creating a Dictionary
    "Name" : "subham",
    "age" : 21,
    "course" : "bca",
    "subjects" : ["Java", "Python", "PHP", "javaScripts"]
}

print(dict_) #Prints the whole Dictionary contents

print(f"Name of the student is {dict_['Name']}") #Accessing the values present in the dictionary using the key
print(f"Age of the student is {dict_['age']} and course is {dict_['course']}")

length_dictionary = len(dict_) #Length of the Dictionary is taken with the help of  len()
print(f"Length of the dictionary is {length_dictionary}")

con_dict = dict(name = "Subham", age = 21, course = "BCA", subjects = ["Java", "Python", "PHP"])
print(con_dict)

name_ = dict_["Name"]
print(name_)

subjects_ = dict_["subjects"]
print(subjects_)

_name = dict_.get("Name")
print(_name)

keys_dict = dict_.keys()
print(keys_dict)

dict_["Laptop"] = "HP"

print(keys_dict)

values_dict = dict_.values()
print(values_dict)

items_dict = dict_.items()
print(items_dict)

if "Name" in dict_:
    print(f"Key Name is present in the dictionary")
else:
    print("Key is not present in the dictionary")

con_dict.update({"name" : "SUBHAM"})
print(con_dict)

dict_.pop("Laptop")
print(dict_)

con_dict.popitem()
print(con_dict)

del con_dict["course"]
print(con_dict)

con_dict.clear()
print(con_dict)

for x in dict_:
    print(x)

for i in dict_:
    print(dict_[i])

for y in dict_.values():
    print(y)

for k  in dict_.keys():
    print(k)

for keys, values in dict_.items():
    print(keys, values)



