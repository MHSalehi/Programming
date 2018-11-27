# ----------------------------------------------------------------------------------------------------------------------
# Strings Exercises
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# 1.)
# ----------------------------------------------------------------------------------------------------------------------

print("\n=== Strings Exercise 1 ===\n")
word1 = "codecode"
word2 = "copecodetreccoe"
word1n = 0
word2n = 0

for i in range(len(word1)-3):
    if word1[i] == "c":
        if word1[i+1] == "o":
            if word1[i+3] == "e":
                word1n += 1

for i in range(len(word2)-3):
    if word2[i] == "c":
        if word2[i+1] == "o":
            if word2[i+3] == "e":
                word2n += 1

print("\'Co_e\' appears " + str(word1n) + " times in " + word1 + ".")
print("\'Co_e\' appears " + str(word2n) + " times in " + word2 + ".")

userInputn = 0
while True:
    userInput = input("\nTest with custom string [Y/N]? ")
    if userInput.lower() not in ["y", "yes", "ok", "okay", "n", "no", "nope"]:
        print("Invalid answer please try again.")
        continue
    if userInput.lower() in ["y", "yes", "ok", "okay"]:
        while True:
            userInput = None
            userInput = input("\nEnter custom string: ")
            for i in range(len(userInput) - 3):
                if userInput[i] == "c":
                    if userInput[i + 1] == "o":
                        if userInput[i + 3] == "e":
                            userInputn += 1
            print("\n\'Co_e\' appears " + str(userInputn) + " times in " + userInput + ".")
            userInput = None
            userInputn = 0
            while True:
                userInput = input("Test again? ")
                if userInput.lower() not in ["y", "yes", "ok", "okay", "n", "no", "nope"]:
                    print("Invalid answer please try again.")
                    continue
                break

            if userInput.lower() in ["y", "yes", "ok", "okay"]:
                continue
            break
    break


# ----------------------------------------------------------------------------------------------------------------------
# 2.)
# ----------------------------------------------------------------------------------------------------------------------

print("\n=== Strings Exercise 2 ===\n")
word1 = "hi Chi a"
word2 = "hihihi"
word1b = 0
word2b = 0

userInputProcessed = 0
userInput = input("Enter a string: ")

for i in range(len(userInput)-1):
    if userInput[i] == "h":
        if userInput[i+1] == "i":
            userInputProcessed += 1

print("\'hi\' appears " + str(userInputProcessed) + " times in " + userInput + ".")


# ----------------------------------------------------------------------------------------------------------------------
# Lists Exercises
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# 1.)
# ----------------------------------------------------------------------------------------------------------------------

print("\n=== Lists Exercise 1 ===\n")
list1 = [3, 4, 4, 5, 5, 6]
list2 = [1, 0, 0, 0, 2, 8, 11]

new_list1 = []
new_list2 = []

lastVal = None

for i in list1:
    if i != lastVal:
        new_list1.append(i)
        lastVal = i
print(new_list1)

for i in list2:
    if i != lastVal:
        new_list2.append(i)
        lastVal = i
print(new_list2)

# or just use: 'if i not in new_list1...' then append.


# ----------------------------------------------------------------------------------------------------------------------
# 2.)
# ----------------------------------------------------------------------------------------------------------------------

print("\n=== Lists Exercise 2 ===\n")
list1 = [1, 2, 2, 1, 13]
new_list1 = []
list2 = [1, 1]
new_list2 = []
list3 = []
new_list3 = []

lastVal = None
for i in list1:
    if i != 13:
        if lastVal != 13:
            new_list1.append(i)
    lastVal = i
print(sum(new_list1))

lastVal = None
for i in list2:
    if i != 13:
        if lastVal != 13:
            new_list2.append(i)
    lastVal = i
print(sum(new_list2))

lastVal = None
for i in list3:
    if i != 13:
        if lastVal != 13:
            new_list3.append(i)
    lastVal = i
print(sum(new_list3))

lastVal = 0
userListFiltered = []
userInput = input("\nEnter a string of numbers: ")
userListRaw = [x.strip() for x in userInput.split(",")]
print(userListRaw)
for i in userListRaw:
    if int(i) != 13:
        if int(lastVal) != 13:
            userListFiltered.append(int(i))
    lastVal = i
print("\nSum of filtered values: ", sum(userListFiltered))

# ----------------------------------------------------------------------------------------------------------------------
# MHS: Why does this only work with user sequences separated by ','?
#      E.g. '1, 5, 1, 89, 1, 5, 13, 4, 4, 3, 5' works,
#      '1 5 1 89 1 5 13 4 4 3 5' does not.
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Extra
# ----------------------------------------------------------------------------------------------------------------------

print("\n=== Extra Exercise ===\n")
tempC = None
tempF = None
tempVal = None

while True:
    userTemp = input("Enter a temperature [Format = <Temp>C/F]: ")
    if userTemp[:-1].isdigit() and userTemp[-1].lower() in ["c", "f"]:
        if userTemp[-1].lower() == "f":
            print("\nFahrenheit detected. Converting to Celsius...")
        if userTemp[-1].lower() == "c":
            print("\nCelsius detected. Converting to Fahrenheit...")
        break

tempVal = userTemp[:-1]

if userTemp[-1].lower() == "c":
    tempF = (float(tempVal) * 9.0 / 5.0 + 32)
    print("That is the same as " + str(round(tempF, 1)) + "F.")
if userTemp[-1].lower() == "f":
    tempC = (float(tempVal) - 32) * 5.0 / 9.0
    print("That is the same as " + str(round(tempC, 1)) + "C.")