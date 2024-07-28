import random

def choose_word():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word.strip()

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts_left = 6
    
    while True:
        print("\nAttempts left:", attempts_left)
        displayed_word = display_word(word, guessed_letters)
        print(displayed_word)
        
        if displayed_word.replace(' ', '') == word:
            print("\nCongratulations! You guessed the word:", word)
            break
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            attempts_left -= 1
            print("Incorrect guess!")
        
        if attempts_left == 0:
            print("\nSorry, you ran out of attempts. The word was:", word)
            break

if __name__ == "__main__":
    hangman()
