import random

ListOfWords = ["anachronistic", "belligerence", "benevolence", "symphony" , "Blasphemous" , "conception" , "Pizza" , "Grandoise", "marionette", "waltzing", "Dislocated", "Enigma", "Aurora Borealis", "Diseducation", "Edutainment"]
random.shuffle(ListOfWords)

Correct = 0
Mistakes = 0

print("Welcome to the talking typeface game")
print("Type the word shown correctly and I might have a prize for you")
print("If you make a mistake im gonna be sad :(")
print("Keep in mind this game is case sensitive")

for word in ListOfWords:
    print(word)
    Input = input("Type the world:")

    if Input == word:
        print("Correct!")
        Correct +=1
    else:
        print("You made a mistake")
        Mistakes +=1

Accuracy = (Correct / len(ListOfWords)) * 100

print("\nGame over")
print("Results:")
print(f"Correct words: {Correct}")
print(f"Mistakes: {Mistakes}")
print(f"Accuracy: {Accuracy:.2f}%")

