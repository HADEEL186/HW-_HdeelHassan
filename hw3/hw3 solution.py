# exercise1
#
# Mydic = {('name, Last_name'): 'Hadeel Hassan', 'age': '31', 'PhoneNumber': '0525787713'}
# print(Mydic)
#
# exercise2

# def replace(mylist):
#     try:
#         len(mylist) > 5
#     except:
#         print("Your list is too short!")
#     else:
#         mylist[5] = "@"
#         return mylist
#
#
# x= replace([1,2,3,4,5,6,7,8,9])
# print(x)

# exercise3

# def func(mylist):
#     assert len(mylist) > 5, "Your list is too short!"
#     mylist[5] = '@'
#     return mylist
#
#
# func([1,2,3,4,5,6,7,8,9])
# print(func([1,2,3,4,5,6,7,8,9]))

# exercise4

# def func(dict1, dict2):
#     dict1.update(dict2)
#     dict2.update(dict1)
#     return (dict1)
#
# dict1 = {'key1': 'Hello', 'key2': 'World'}
# dict2 = {'key3': 'Python'}
# print (func(dict1, dict2))
# #
# exercise5

# dict = {}
# n = 5
# for x in range(1,n+1):
#     dict[x]=x+3
# print(dict)

# exercise6
# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}
# dict4 = {}
# for x in (dict1, dict2, dict3):
#     dict4.update(x)
# print(dict4)

# exercise7

# dict1 = {}
# def func(mystr):
#     for char in mystr:
#         count = dict1.get(char, 0)
#         count += 1
#         dict1[char] = count
#     chars = dict1.keys()
#     chars = sorted(chars)
# func("hadeelhassan")
# print(dict1)

#  exercise8
#


def func(dict1, dict2):
    dict3 = {}
    for key1 in dict1:
        if key1 in dict2:
            dict3.update({key1: ((dict1[key1] + dict2[key1]))})
        else:
            dict3.update({key1: dict1[key1]})
    for key2 in dict2:
        if key2 not in dict1:
          dict3[key2] = dict2[key2]
    return (dict3)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 4, 'e': 5, 'c': 6}
print(func(dict1, dict2))