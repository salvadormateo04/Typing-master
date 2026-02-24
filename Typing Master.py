import random

ListOfWords = ["anachronistic", "belligerence", "benevolence", "symphony" , "Blasphemous" , "conception" , "Pizza" , "Grandoise", "marionette", "waltzing", "Dislocated", "Enigma", "Aurora Borealis", "Diseducation", "Edutainment"]
random.shuffle(ListOfWords)

WordCount = 15

try:
    Correct = 0
    Mistakes = 0

    for word in ListOfWords:
        print("Welcome to the talking typeface game")
        print("Type the word shown correctly and I might have a prize for you")
        print("If you make a mistake im gonna be sad :(")
        print("Keep in mind this game is case sensitive")

        print({word})
        Input = input("Type the following world:")

        if Input == word:
            print("Correct!")
            Correct =+1

        if wordCount == 1:
            print("Game over")

except Exception as e:
    print("An unexpected error occurred:", e)
