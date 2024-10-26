questions = ("How many planets are there?",
             "Who are you?",
             "What are you?",
             "What is your homeland?",
             "Who owns the world?")

options = (("A. 13", "B. 10", "C. 6", "D. 8"), 
           ("A. Ramie", "B. Ramie The Great", "C. Just a man", "D. I am Spartacus!"), 
           ("A. Just a man", "B. A ruler", "C. A God", "D. The chosen one"), 
           ("A. Syria", "B. Damascus", "C. Canada", "D. The entire world"), 
           ("A. Satanists", "B. America", "C. Jews", "D. Ramie Mosely The Great",))

answers = ("D", "D", "D", "D", "D")

questionNum = 0


guesses = []

score = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[questionNum]:
        print(option)

    guess = input("Please enter your choice: \n").upper()
    guesses.append(guess)
    if guess == answers[questionNum]:
        score += 1
        print("HELL YEAH!")
    else:
        print("Think again!")
        print(f"{answers[questionNum]} is the correct answer!")

    questionNum += 1



print("--------------------")
print("       RESULTS      ")
print("--------------------")

print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
 
score = int(score / len(questions) * 100)
print(f"Your score is {score} %")






