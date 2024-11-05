import random as rand
random_word = rand.randint(1,3)

alfabet = list("abcdefghijklmnopqrstuvwxyzåäö")
guessed_letters = list("")

if random_word == 1:
    word = "hus"
elif random_word == 2:
    word = "stora"
else:
    word = "pannkaka"

lives = 5

word_letters = list(word)

while lives > 0:
    for char in word_letters:
        if char in alfabet:
            print("*", end="")
        else:
            print(char, end="")
    print("")
    
    guessed_letters.append(input("gissa en bokstav"))
    for chars in guessed_letters:
        if chars in alfabet:
            alfabet.remove(chars)
    print("gissade bokstäver", guessed_letters)

    if chars not in word_letters:
        lives= lives - 1
    print("liv kvar:", lives)


if lives < 1:
    print("du förlora")