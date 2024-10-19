import time

name = input("Please enter your name!\n")
name = name.lower()
lookFor = input("What character would you like to look for?\n")
replace = input("What would you like to replace it with?\n")
resultLen = len(name)

#First occurence
resultFind = name.find(lookFor)

#Last occurence
resultFindR = name.rfind(lookFor)

#Checks if string contains only digits, returns boolean
resultIsDigit = name.isdigit()

#Count method checks how many occurences character
resultOccurence = name.count(lookFor)

#Replaces
resultReplace = name.replace(lookFor, replace)

print(f"The length of your input is {resultLen} characters long")
time.sleep(0.5)
print(f"The first instance of the character you want occurs at index {resultFind}")
time.sleep(0.5)
print(f"Is the input only digits? {resultIsDigit}")
time.sleep(0.5)
print(f"The character you want occurs {resultOccurence} times")
print(f"The character you want to replace: {resultReplace}")
time.sleep(1)
#print(help(str))


#Validate user input
#1. Username is no more than 12 characters long
#2. Username must not contain spaces
#3. Username must not contain digits.


def validateUserInput():

    userValid = False

    while userValid == False:
        userInput = input("Please enter a valid username!")
        checkLength = len(userInput)
        checkSpaces = userInput.find(" ")
        checkAlpha = userInput.isalpha()


        if checkLength <= 12 and checkSpaces == -1 and checkAlpha == True:
            print(f"Welcome {userInput}!")
            userValid = True



validateUserInput()