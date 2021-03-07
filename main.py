import random


def selectRandomWord():
    with open("english2.txt", "r") as myNewFile:
        randomNumber = random.randint(1,65000)
        for lineIndex,line in enumerate(myNewFile):
            if lineIndex == randomNumber:
                return line.replace("/n","").replace(" ","").upper()
            
def guessingLetter(randomWord):
    print(randomWord)
    numberOfLives = 5
    theirGuess = ["_" for x in range(len(randomWord)-1)]
    while numberOfLives > 0:
        print(f"this is your current gueesing board {theirGuess}")
        whatletter = input(f"Pick a letter that may be in your word").upper()
        if len(letterPlacement(theirGuess,whatletter)) > 0:
            print("you have already guessed this. However no lives will be taken off")
            continue
        letterPlacementIndexArray = letterPlacement(randomWord,whatletter)
        if(len(letterPlacementIndexArray) > 0):
            for solutionIndex in range(len(letterPlacementIndexArray)):
                theirGuess[letterPlacementIndexArray[solutionIndex]] = whatletter
            print("congrarts that letter was correct!")
            if len(letterPlacement(theirGuess,"_")) == 0:
                print(f"you have won the game, the final word is {randomWord}")
                return
        else: 
            numberOfLives = numberOfLives - 1
            print(f"Unlucky, that guess was incorrect, you now have {numberOfLives} lives.")
        
    print(f"Unlucky, the word was actually {randomWord}")



        
        
def letterPlacement(randomWord,letter):
    letterIndexs = []
    for letterIndex in range(len(randomWord)):
        if letter == randomWord[letterIndex]:
            letterIndexs.append(letterIndex)
    return letterIndexs
        

def main():
    randomWord = selectRandomWord() 
    print(f"your word is {len(randomWord)-1} letters long")
    guessingLetter(randomWord)


main()

#1)Fix letterPlacement function to find all isntances
#2)Fix repeating letters




# letterPlacement()
    # for whatLetter in range(len(randomWord)):
    #     if whatletter == (randomWord()):
    #         print(f"{len(randomWord-1.replace 'randomWord','-')}")
    #     if whatletter != (randomWord(0,len)):
    #     
    # return
    # if whatLetter == letter:
    #     print(f"you have got the word. It was {randomword}")