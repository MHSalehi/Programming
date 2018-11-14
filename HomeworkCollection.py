# ----------------------------------------------------------------------------------------------------------------------
# Homework Collection
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Strings Review - Exercise 1
# ----------------------------------------------------------------------------------------------------------------------

# hey = "Hey, it's Jo!"
# there = "there"
#
# 1) Hey,
# 2) !
# 3) Hey, it's Jo!Hey, it's Jo!
# 4) Hey, it's Jothere!
# 5) Hey, it's Jo there!
# 6) h
# 7)
# 8) Hey, it's Jo!Hey, it's Jo!therthere!
# 9)


# ----------------------------------------------------------------------------------------------------------------------
# Strings Review - Exercise 2
# ----------------------------------------------------------------------------------------------------------------------

# Date Format: dd/mm/yyyy

# while True:
#     userDate = input("Please provide a date using the format 'dd/mm/yyyy': ")
#     userDelimitedDate = userDate.split("/")
#     if 31 >= int(userDelimitedDate[0]) > 0 and 12 >= int(userDelimitedDate[1]) > 0:
#         break
#
# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
#           "November", "December"]
#
# outputDate = []
#
# formatMonth = months[(int(userDelimitedDate[1]) -1)]
# outputDate.append(str(formatMonth))
# outputDate.append(str(userDelimitedDate[0]))
# outputDate.append(str(userDelimitedDate[2]))
#
# outputDateString = str(outputDate)
# print("The date is " + " ".join(outputDate))


# ----------------------------------------------------------------------------------------------------------------------
# Lists Review - Exercise 1
# ----------------------------------------------------------------------------------------------------------------------

# a_list = [3, 5, 6, 12]
#
# # 1.
# print(a_list[0])
#
# # 2.
# from operator import itemgetter
# print(*itemgetter(1, 2, 3)(a_list))
#
# # 3.
# print(itemgetter(3, 2, 1, 0)(a_list))
#
# # 4.
# print(a_list[0]**2, a_list[0]*a_list[1], a_list[0]*a_list[2], a_list[0]*a_list[3])

# ----------------------------------------------------------------------------------------------------------------------
# Comment: For the above, is there another way to achieve this w/o repeating, "a_list[i]" repeatedly?               X
# ----------------------------------------------------------------------------------------------------------------------

# # 5.
# evenCheck = []
# for i in a_list:
#     if i % 2 == 0:
#         evenCheck.append("True")
#     else:
#         evenCheck.append("False")
#
# print(evenCheck)


# ----------------------------------------------------------------------------------------------------------------------
# Lists Review - Exercise 2
# ----------------------------------------------------------------------------------------------------------------------

# import re
# while True:
#     userNumbers = input("Please enter 5 numbers separated with single spaces: ")
#     userList = re.split("  | |, |,", userNumbers)
#     print(userList)
#     if len(userList) == 5:
#         break
#     else:
#         print("\nYou didn't enter 5 numbers." + "\n")
#
# userOddNumbers = []
# for i in userList:
#     if int(i) % 2 != 0:
#         userOddNumbers.append(i)
#
# print("\nYour odd numbers: ",*userOddNumbers)

# ----------------------------------------------------------------------------------------------------------------------
# Comment: Seeing one extra space on the line 231 print function after, "Your odd numbers:__" <- here.              X
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Lists Review - Exercise 3                                                                                         X
# ----------------------------------------------------------------------------------------------------------------------

# myList = ["axe", "dagger", "oranges"]
# newList = [insert for item in myList for insert in ("*", item)]
# print(newList)


# ----------------------------------------------------------------------------------------------------------------------
# Dictionaries Review - Exercise 1
# ----------------------------------------------------------------------------------------------------------------------

#    # "Write a Python script to print a dictionary where the keys are numbers
#    # between 1 and 15 (both included) and the values are square of keys."
#
# scriptDict = {}
# for i in range(1,16):
#     scriptDict[i] = i**2
# print(*scriptDict.items())


# ----------------------------------------------------------------------------------------------------------------------
# Dictionaries Review - Exercise 2
# ----------------------------------------------------------------------------------------------------------------------

#    # "The following Dictionary includes some duplicate
#    # value entries. Write a program to remove them."
#
# room_items = {"item1" :
# {"Name" : "Lamp", "Colour" : "Red"}, "item2" :
# {"Name" : "Table", "Colour" : "Brown", "Type": 0}, "item3" :
# {"Name" : "Lamp", "Colour" : "Red"}, "item4" :
# {"Name" : "Chair", "Colour" : "Green", "Type" : 1}
# }
#
# newList = {}
#
# for key, value in room_items.items():
#     if value not in newList.values():
#         newList[key] = value
#
# print(newList)


# ----------------------------------------------------------------------------------------------------------------------
# Dictionaries Review - Exercise 3
# ----------------------------------------------------------------------------------------------------------------------

#   Please see file, "HomeworkInventoryExercise.py" on GitHub.


# ----------------------------------------------------------------------------------------------------------------------
# Conditionals & Loops Review - Exercise
# ----------------------------------------------------------------------------------------------------------------------

#   Please see file, "HomeworkTextAdvent.py" on GitHub.