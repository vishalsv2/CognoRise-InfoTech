import random

def hangman():
    word_list = ["python", "java", "hangman", "game"]
    random_word = random.choice(word_list)
    guessed_letters = []
    attempts = 6

    print("Let's play Hangman!")
    print('_ ' * len(random_word))

    while attempts > 0:
        guess = input("\nPlease guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter.")
        elif guess in guessed_letters:
            print("You have already guessed this letter.")
        elif guess not in random_word:
            print("This letter is not in the word.")
            attempts -= 1
        else:
            print("Good job! This letter is in the word.")
            guessed_letters.append(guess)

        word_completion = [letter if letter in guessed_letters else '_' for letter in random_word]
        print(' '.join(word_completion))

        if '_' not in word_completion:
            print("Congratulations, you won!")
            return

    print("Sorry, you ran out of attempts. The word was " + random_word + ". Better luck next time!")

hangman()
