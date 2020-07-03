import random

print("\n\t\t\t\tHOGWARTS THEMED HANGMAN GAME!\n")
name = input("Enter your name: ")
print("\nWelcome "+name+"!\nLet's test whether you're a true Potterhead or not :)\n")
words = ['HARRY', 'DEMENTORS', 'SNITCH', 'HOGWARTS', 'HERMOINE', 'RON', 'QUIDDITCH', 'POMFREY', 'WAND', 'ROBES', 'DUMBLEDORE', 'MUGGLE', 'POTIONS', 'SNAPE', 'HAGRID', 'BUTTERBEER', 'AZKABAN', 'MUDBLOOD', 'MCGONNAGAL', 'CHAMBER', 'HALFBLOOD', 'DRACO', 'DOBBY', 'MARAUDERER', 'MALFOY', 'VOLDEMORT', 'PRISONER', 'GOBLET', 'SORCERER', 'DURSLEY', 'HEDWIG', 'WEASLEY', 'DIAGONALLEY', 'GINNY', 'TROLL', 'CHARM', 'LONGBOTTOM', 'GRYFFINDOR', 'HUFFLEPUFF', 'RAVENCLAW', 'SLYTHERIN', 'CLOAK', 'ARAGOG', 'LOCKHART', 'MYRTLE']

word = random.choice(words)
letter = random.choice(list(word))
turns = 10
guess = word

def hangman(turns):
    if turns == 9:
        print("____________\nTurns left: ",turns)
    elif turns == 8:
        print("____________")
        print("     O      \nTurns left: ",turns)
    elif turns == 7:
        print("____________")
        print("     O      ")
        print("     |      \nTurns left: ",turns)
    elif turns == 6:
        print("____________")
        print("    \O      ")
        print("     |      \nTurns left: ",turns)
    elif turns == 5:
        print("____________")
        print("    \O      ")
        print("     |      ")
        print("    /       \nTurns left: ",turns)
    elif turns == 4:
        print("____________")
        print("    \O/     ")
        print("     |      ")
        print("    /       \nTurns left: ",turns)
    elif turns == 3:
        print("____________")
        print("    \O/     ")
        print("     |      ")
        print("    / \     \nTurns left: ",turns)  
    elif turns == 2:
        print("____________")
        print("    \O/ |   ")
        print("     |      ")
        print("    / \     \nTurns left: ",turns)
    elif turns == 1:
        print("____________")
        print("    \O_|    ")
        print("     |\     ")
        print("    / \     \nTurns left: ",turns)
    elif turns == 0:
        print("____________")
        print("     O_|    ")
        print("    /|\     ")
        print("    / \     ")
        print("YOU'RE DEAD! .. YOU LOST THE GAME!\n")
        exit()

for i in guess:
    if i!=letter:
        guess = guess.replace(i, '-')

print("\t\t\t\t  Guess the word? " + guess + "\n\t\t\t   You have "+str(turns)+" turns to guess the word.\n")
score = turns
while True:
    alpha = input("Enter the guessed alphabet: ").upper()
    if alpha in word and alpha not in guess:
        if word.count(alpha) > 1:
            indx_postn = 0
            indx_list = []
            for i in range(word.count(alpha)):
                indx_postn = word.index(alpha, indx_postn)
                indx_list.append(indx_postn)
                indx_postn+=1
            for i in indx_list:
                guess = list(guess)
                guess.pop(i)
                guess.insert(i, alpha)

            print(''.join(guess))
            if (''.join(guess)) == word:
                print("YOU WON!")
                break
        else:
            indx = word.index(alpha)
            guess = list(guess)
            guess.pop(indx)
            guess.insert(indx, alpha)
            print(''.join(guess))
            if (''.join(guess)) == word:
                print("YOU WON!")
                break
    else:
        score -= 1
        hangman(score)