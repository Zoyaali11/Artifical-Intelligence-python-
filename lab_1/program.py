print("Welcome to the Simple Word Game!")
word_to_guess = "python"
correct_guess = False

def display_hint():
    print("Here's a hint: It's a programming language.")

def check_guess(user_guess):
    return user_guess.lower() == word_to_guess

hint_list = ["It starts with 'p'", "It is a programming language"]

info = ("This is a simple word game.", "You have to guess the word.")

print("Hints List:", hint_list)

play = input("Do you want to play the word game? (yes/no): ")

if play.lower() == "yes":
    print("Great! Let's start the game.")
    display_hint()
else:
    print("No worries! Goodbye for now!")
    exit()

print("Extra Information:", info)

for hint in hint_list:
    print("Hint:", hint)

while not correct_guess:
    user_input = input("Guess the word: ")
    correct_guess = check_guess(user_input)
    if not correct_guess:
        print("Incorrect guess. Try again!")

print("Congratulations! You guessed the word correctly.")

print("\nEnd of the Word Game.")


