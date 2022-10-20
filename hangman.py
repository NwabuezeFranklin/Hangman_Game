import random
print("""H A N G M A N\n""")
listed = ['python', 'java', 'swift', 'javascript']
correct = random.choice(listed)
#split = "-"*(len(correct))
#splitter = list(split)
attempt = 0
#attempted = []
loss = 0
win = 0

def validate():
    while True:
        print(split)
        ch = (input(f'Input a letter:'))
        if (len(ch) > 1) or (len(ch) < 1):
            print("Please, input a single letter")
        elif (ch>='a' and ch<= 'z'):
            break
        elif (ch>='A' and ch<='Z'):
            print("Please, enter a lowercase letter from the English alphabet.")
        else:
            print("Please, enter a lowercase letter from the English alphabet.")
    return ch

while True:
    decision = input(f'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if decision == 'play':
        split = "-" * (len(correct))
        attempted = []
        splitter = list(split)
        while attempt <= 8:
            if split == correct:
                print(f'You guessed the word {correct}!\n'
                      f'You survived!')
                win += 1
                break
            userInput = validate()
            if userInput not in attempted:
                if userInput in correct:
                    position = [pos for pos, char in enumerate(correct) if char == userInput]
                    for i in range(len(position)):
                        splitter[position[i]] = userInput
                    split = "".join(splitter)
                else:
                    print("That letter doesn't appear in the word.")
                    attempt += 1
            else:
                print("You've already guessed this letter.")
                attempt += 1
            attempted.append(userInput)

            if attempt == 8:
                print("\nYou lost!")
                loss += 1
                break
    elif decision == 'results':
        print(f'You won: {win} times.\n'
              f'You lost: {loss} times.')
    else:
        break


