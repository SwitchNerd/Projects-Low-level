#Hangman game #1
import random
wordsList = ['random','word','dog','stair','fork','python']
wordChosen = ''
wordLength = 0
wordPrinted = ''
chances = 5
def checkWord(letter, word):
    
    return word.rfind(letter)
    
def pMan(chances):
    match chances:
        case 0:
            print('----')
            print('|  |')
            print('|')
            print('__')
        case 1:
            print('----')
            print('|')
            print('|')
            print('__')
        case 2:
            print('|')
            print('|')
            print('__')
        case 3:
            print("|")
            print("__")
        case 4:
            print("__")


print("Game Start...!")
print('')
wordChosen = wordsList[random.randrange(1,6)]
wordLength = len(wordChosen)
for i in range(wordLength):
    wordPrinted += '_'
print(wordPrinted)
wordPrinted = list(wordPrinted)
print('')
print(wordChosen)
while chances != 0:

    letter = input('Enter a letter: ')
    if letter[1]:
        print('You have broken the rules 🤡! GAME OVER')
        break
    result = checkWord(letter , wordChosen)
    if result == -1:
        chances = chances - 1
        print(f'You have {chances} chance/s left.')
        pMan(chances)
    else:
        wordPrinted[result] = letter

        printthis = ''.join(str(x) for x in wordPrinted)
        print(printthis)
        if '_' not in printthis:
            print("You have won ! 🎗️👌🎯")
            break