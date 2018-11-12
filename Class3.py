# ----------------------------------------------------------------------------------------------------------------------
# Sorting Lists
# ----------------------------------------------------------------------------------------------------------------------

# x = ["mix", "xyz", "apple", "xanadu", "rovio"]
#
# newList_a = []
# newList_b = []
#
# for word in x:
#     if word[0] == "x":
#         newList_a.append(word)
#     else:
#         newList_b.append(word)
#
# print(*(sorted(newList_a)+sorted(newList_b)))


# ----------------------------------------------------------------------------------------------------------------------

# numbers = [2, 3, 5, 7, 66 , 89, 134]
#
# userInput = int (input ("Give me an upper limit number: "))
# newList = []
#
# for x in numbers:
#     if x <= userInput:
#         newList.append(x)
#
# print("\nNumbers in range: ")
# print(newList)
#
# # Print list interspaced with "*" symbols   #### Need to convert to string first!
# a = [x**2 for x in range(5)]
# print(*a)
# b = "-".join(str(a))
# print(b)
#
# tupleList_A = [ (), (), ("",), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# tupleList_B = []
# for i in tupleList_A:
#     # if a:
#     #     tupleList_B.append(i)
#     if len(i) != 0 and not ______:
#         tupleList_B.append(i)
#     #if len(i) != 0 and i != " ":
#     #    tupleList_B.append(i)
# print(tupleList_B)

# ----------------------------------------------------------------------------------------------------------------------
# Dictionaries
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Dictionary Commands
# ----------------------------------------------------------------------------------------------------------------------

# # my_Dict.keys() --- returns the list of keys
# # my_Dict.values() --- returns the list of values
# # my_Dict.items()  ---  returns a list of all key/item pairs

# ----------------------------------------------------------------------------------------------------------------------


# my_Dict = {"John": 17, "Jane": 19, "Doggo": 4}
# print(my_Dict["Doggo"])
# print(my_Dict["John"])
#
# # Can use Dictionary values as room descriptors - reference the relevant index for a given room to print a
# description/options? Use to update rooms perhaps?
#
# # Dictionary keys must be immutable
#
# # my_Dict.keys() --- returns the list of keys
# # my_Dict.values() --- returns the list of values
# # my_Dict.items()  ---  returns a list of all key/item pairs
#
# print(my_Dict.values())


# ----------------------------------------------------------------------------------------------------------------------
# Misc.
# ----------------------------------------------------------------------------------------------------------------------

# myDict = {"A": 2, "B": 4, "C": 6, "D": 8}
# for key in myDict:
#     print(key + str(myDict[key]))
