import random

# Define words and their categories
word_categories = {
    'fruits': 'apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon',
    'animals': 'dog cat elephant lion tiger giraffe kangaroo penguin zebra dolphin platypus parrot owl panda koala',
    'colors': 'red blue green yellow orange purple pink brown black white grey silver gold indigo maroon turquoise',
}

def choose_category():
    while True:
        print('Available categories:')
        for category in word_categories:
            print(f'{category.capitalize()}')
        selected_category = input('Choose a category to guess words from: ').lower()
        if selected_category in word_categories:
            return selected_category
        else:
            print('Invalid category. Please try again.')

def choose_word(category):
    words = word_categories[category].split()
    return random.choice(words)

def main():
    category = choose_category()
    word = choose_word(category)

    print(f'Guess the word from the {category} category!')

    word_length = len(word)
    display_word = ['_'] * word_length

    playing = True
    correct_guesses = []
    incorrect_guesses = []
    chances = len(word) + 5
    flag = 0

    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            guess = input('Enter a letter to guess: ').lower()

            if len(guess) != 1 or not guess.isalpha():
                print('Please enter a single letter.')
                continue

            if guess in correct_guesses:
                print('You have already guessed that letter.')
                continue
            elif guess in incorrect_guesses:
                print('You have already guessed that letter incorrectly.')
                continue

            if guess in word:
                for i in range(word_length):
                    if word[i] == guess:
                        display_word[i] = guess
                correct_guesses.append(guess)
            else:
                incorrect_guesses.append(guess)

            print(' '.join(display_word))

            if '_' not in display_word:
                print(f"The word is: {word}")
                flag = 1
                print('Congratulations, You won!')
                break

        if chances == 0 and '_' in display_word:
            print()
            print('You lost! Try again..')
            print(f'The word was: {word}')

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')

if __name__ == '__main__':
    main()
