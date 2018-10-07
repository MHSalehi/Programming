#Introduction, Printing Strings
print ("Hello, Python!")

spch = "Greetings!"
print (spch + " What is your name?")

#Practicing with .upper() and .lower() functions
t = "Barry ProgrammeR"
print (t[-3].upper() + t[-2] + t[2:5] + (" ") + t[7].upper() + t[8] + t[-5:-3] + t[-2] + t[-1].lower())

#Print Character Count
print ("Number of characters in " + "'" + str(t) + "'" + " = " + str(len(t)))

#Strip Function Experimentation
print ("\n")
a = "     Stripping a sentence.        "
print ("No stripping:" + "'" + a + "'")
print ("After stripping white space: " + "'" + a.strip() +  "'")
print ("After stripping words: " + "'" + a.strip(" Stripping" "sentence. ") + "'" )

#Testing for alphabet/digit/space-only character strings
print ("\n")
b = "Alpha"
print (b.isalpha())
c = "Alpha1"
print (c.isdigit())
d = "\n "
print (d.isspace())

#Testing for strings beginning and ending in specific strings
print ("\n")
e = "All aboard the typing train."
print (e.startswith("All"))
print (e.endswith("train."))
print (e.endswith("in", -7, -1))
print (e.endswith("in", -12, -8))

#Searching for a specific string within another string
print ("\n")
print (e.find("aboard"))
print (e.find("abort"))

#Substituting portions of a string
print ("\n")
print (e.replace("All aboard", "Expedite"))

#User inputs
name = input("what is your name? ")
age = int(input("What is your age? "))

#Conditional Checks
print("\n")
if age >= 35:
    print("With age comes wisdom.")
elif age >= 25:
    print("The tip of the iceberg.")
elif age >= 15:
    print("So much to learn.")
else:
    print("Just getting started.")

#Conditional Class Task 3
print("\n")
playernum = int(input("Choose a number: "))
if playernum <= 100:
    print ("That's a small number.")
elif playernum <= 1000:
    print ("That's an adequately huge number!")

#Conditional Class Task 4
n = playernum % 2
if n == 0:
    print ("This an even number.")
else:
    print ("This is an odd number.")
