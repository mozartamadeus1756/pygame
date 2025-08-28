import random
from art import stages

random_words = ["basketball", "football", "tennis", "badminton", "swimming", "track", "golf", "kayaking"]

chosen_word = random.choice(random_words)
word_length = len(chosen_word)

end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("guess the letter: ").lower()
    
    if guess in display:
        print(f'you have already guessed {guess}')
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives -= 1
        print(f'you guessed {guess}, thats not in the word you lose a life !!!')
        
        if lives == 0:
            end_of_game = True
            print("you lose !! ")
    
    print(f"{''.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("you win !!")
    
    print(stages[lives])