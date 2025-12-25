''' # Multi-line docstring comment explaining what sets are
Sets are used to store multiple items in a single variable. # Explanation that sets store multiple items

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage. # Describes sets as one of 4 built-in collection types

A set is a collection which is unordered, unchangeable*, and unindexed. # Explains key characteristics of sets
''' # End of multi-line docstring comment

myset = {1, 2, 3} # Creates a set with three integer values (values must be unique, no duplicates allowed)
print(myset) # Prints the contents of myset to the console

duplicate_set = {2, 7, 8, 9, 7} # Creates a set with duplicate value 7, which will be automatically removed (sets ignore duplicates)
print(duplicate_set) # Prints the set after duplicate removal

my_set = {"apple", True, 1, "My name is Subham"} # Creates a set with mixed data types (note: 1 and True are considered the same value in sets)
print(my_set) # Prints the set (note: 1 and True are treated as the same value, so only one will appear)

myset_ = {"apple", False, 0, "My name is Subham"} # Creates another set with mixed types (note: 0 and False are considered the same value in sets)
print(myset_) # Prints the set to verify the contents

length_ = len(myset_) # Calculates and stores the number of elements in myset_ (provides the length of the set)
print(length_) # Prints the length of the set

print(type(myset_)) # Prints the data type of myset_ (should be <class 'set'>)

create_set = set(("apple", "banana", "cherry")) # Creates a set from a tuple using the set() constructor
print(create_set) # Prints the newly created set

for s in myset_: # Iterates through each element in myset_
    print(s) # Prints each element of the set on a separate line

print("banana" in create_set) # Checks if "banana" exists in create_set and prints True/False

print("apple" not in create_set) # Checks if "apple" does NOT exist in create_set and prints True/False

create_set.add("orange") # Adds the string "orange" as a new element to create_set
print(create_set) # Prints the set after adding "orange"


myset_.update(create_set) # Updates myset_ by adding all elements from create_set (union operation)
print(myset_) # Prints myset_ after the update operation

myset_.remove("orange") # Removes "orange" from myset_ (raises KeyError if element doesn't exist)
print(myset_) # Prints myset_ after removing "orange"


myset_.discard("apple") # Removes "apple" from myset_ if it exists (doesn't raise error if element doesn't exist)
print(myset_) # Prints myset_ after discarding "apple"

AI_models = {"Chatgpt", "Gemini", "Perplexity", "Nano-Banana" } # Creates a new set containing AI model names
print(AI_models) # Prints the AI_models set
Ai_modelName = AI_models.pop() # Removes and returns a random element from AI_models (pop() randomly removes an item from the set)
print(Ai_modelName) # Prints the element that was popped from the set
print(AI_models) # Prints the remaining elements in AI_models after pop operation

AI_models.clear() # Removes all elements from AI_models, making it an empty set
print(AI_models) # Prints the empty set (should show set())

del AI_models # Deletes the AI_models variable completely from memory

#Joining of SETS (2) # Comment explaining that the following code demonstrates joining two sets

set1 = {"Apple", "Banana", "Cherry"} # Creates the first set with fruit names
set2 = {1, 2, 3} # Creates the second set with integer values
set3_union = set1.union(set2) # Creates a new set containing all unique elements from both set1 and set2
print(set3_union) # Prints the union of set1 and set2

setA = set1 | set2 # Performs union operation using the pipe operator (|) shorthand for union
print(setA) # Prints the result of the union operation using pipe operator

#Joining multiple SETs. # Comment explaining that the following code demonstrates joining multiple sets

setM = set1.union(set2, my_set, myset_) # Joins set1 with set2, my_set, and myset_ into a single set
print(setM) # Prints the union of all specified sets


setM_ = set1 | set2 | setM # Performs union of set1, set2, and setM using pipe operator chaining
print(setM_) # Prints the result of chained union operations

tuple_ = ("subham", "Viraj") # Creates a tuple with two string values
set_t = set1.union(tuple_) # Joins set1 with elements from the tuple (union can accept iterables)
print(set_t) # Prints the union of set1 and tuple elements


setIntersection = set1.intersection(set2) # Finds common elements between set1 and set2 (result will be empty set)
print(setIntersection) # Prints the intersection (common elements) of set1 and set2

setIntersection_ = set1 & set2 # Performs intersection using the ampersand (&) operator shorthand
print(setIntersection_) # Prints the intersection result using ampersand operator

set_difference = set1.difference(set2) # Finds elements in set1 that are not in set2
print(set_difference) # Prints the difference (elements unique to set1)

_setDifference = set1 - myset_ # Performs set difference using the minus (-) operator shorthand
print(_setDifference) # Prints the difference result using minus operator


new_set = {"Subham", "Viraj"} # Creates a new set with two names
NewSet = {"Kundu", "Chakraborty"} # Creates another set with two surnames
set_symmetricDifference = new_set.symmetric_difference(NewSet) # Finds elements in either set but not in both (XOR operation)
print(set_symmetricDifference) # Prints the symmetric difference (all elements except common ones)

setSymmetricDifference = new_set ^ NewSet # Performs symmetric difference using the caret (^) operator shorthand
print(setSymmetricDifference) # Prints the symmetric difference using caret operator

# frozenset is an immutable version of a set. # Comment explaining what frozenset is
# # Empty comment line for spacing
# Like sets, it contains unique, unordered, unchangeable elements. # Explains frozenset characteristics
# # Empty comment line for spacing
# Unlike sets, elements cannot be added or removed from a frozenset. # Explains the key difference from regular sets

x = frozenset({"apple", "banana", "cherry"}) # Creates an immutable frozenset from the given elements
print(x) # Prints the frozenset
print(type(x)) # Prints the data type of x (should be <class 'frozenset'>)

