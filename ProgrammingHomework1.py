#Problem Solving V
playerstr = input("Enter a string: ")
if len(playerstr) >= 3 and (playerstr.endswith("ing")) != True:
        print (playerstr + "ing")
elif playerstr.endswith("ing") == True:
    print (playerstr + "ly")
else:
    print (playerstr)
