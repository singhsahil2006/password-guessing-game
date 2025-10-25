import random
easy_words=['cat', 'dog', 'fish', 'bird', 'tree']
medium_words=['python', 'jumble', 'easy', 'difficult', 'answer']
hard_words=['xylophone', 'quizzical', 'pneumonia', 'juxtapose', 'mnemonic']
print("Welcome to the Password Guessing Game!")
print("Select Difficulty Level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")
level=input("Enter 1, 2, or 3: ").lower()
if level=='1' or level=='easy':
    word=random.choice(easy_words)
elif level=='2' or level=='medium':
    word=random.choice(medium_words)
elif level=='3' or level=='hard':
    word=random.choice(hard_words)
else:
    print("Invalid selection. Defaulting to Easy level.")
    word=random.choice(easy_words)
attempts=0
print("\nGuess the password!")
while True:
    guess=input("Enter your guess: ")
    attempts+=1
    if guess==word:
        print(f"Congratulations! You've guessed the password '{word}' in {attempts} attempts.")
        break
    else:
        print("Incorrect guess. Try again.")
    hint=""
    for i in range(len(word)):
        if i < len(guess) and guess[i] == word[i]:
            hint += word[i]
        else:
            hint += "_"
    print("hint:", hint)
print("Thank you for playing the Password Guessing Game!")