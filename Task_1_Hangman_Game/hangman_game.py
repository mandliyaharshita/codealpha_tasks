import random

# List of 5 predefined words
words = ["python", "coding", "computer", "program", "developer"]

# Select a random word
word = random.choice(words)

# Store correctly guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_wrong_guesses = 6
wrong_guesses = 0

# Display the hidden word
display = ["_"] * len(word)

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while wrong_guesses < max_wrong_guesses and "_" in display:

    print("\nWord:", " ".join(display))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Check whether input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether letter is in the word
    if guess in word:
        print("✅ Correct guess!")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        wrong_guesses += 1
        print("❌ Incorrect guess!")

# Game result
if "_" not in display:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", word)
else:
    print("\n😔 Game Over!")
    print("The word was:", word)
