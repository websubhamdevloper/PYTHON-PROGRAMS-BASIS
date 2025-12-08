
# For Loops

num = 5
for i in range(0, num):
    print(i)

name = "subham"
for i in name:
    print(i)

list_array = [1, 8, 9]
for i in list_array:
    print(i)

tuple_array = (1, 9, 5)
for i in tuple_array:
    print(i)

set1 = {3, 7, 10}
for i in set1:
    print(i)

dictionary_array = dict({'x' : 1288, 'u' : 750})
for i in dictionary_array:
    print("%s %d" % (i, dictionary_array[i]))



for index in range(len(list_array)):
    print(list_array[index])

for letter in name:
    if letter == 'u' or letter == 'a':
        continue
    else:
        print(letter)

for letter in name:
    if letter == 'u' or letter == 'a':
        break
    else:
        print(letter)
#While Loops

number = 0
while number < 5:
    number += 1
    print(number)

#Nested Loop

for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()



