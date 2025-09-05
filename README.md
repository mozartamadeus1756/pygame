# pygames !!! 

ive made a lot of diffrenet pygames and eazy tutorials on how ot make and play them yeyy

her er en oversikt over alle tutorials:
- [pygames !!!](#pygames-)
  - [guessing game !](#guessing-game-)
  - [hangman !](#hangman-)  
  - [snake](#snake) 


## guessing game !
the purpose of this game is to guess waht number the randomiser has chosen. in the code i also set a limit of guesses, so you cant forever, and it makes the game a bit easier !! so lets go thru how i made it:

in this code im using an import aka a libary, and so i place that at the top of the code:
```python
import random
```

secondly you start with a introduction, so the user unserstand whats about to happen: 
```python
print("this is the number guessing game !!") # and so on ...
```

to make the game easier, we put a limit to how big the range of numbers are: 
```python
low = int(input("now you have to choose in whatt range you want to guess the numbers, so enter the lowest range: "))
high = int(input("and now the highest number u want: "))

print(f'now you have 10 chances to guss the numbers from {low} to {high}, good luck !!')
```

now, you have to choose the number that will be generated when the code starts, and the chances you get, like here: 
```python
num = random.randint(low,high)

chances = 10
guesses = 0
```

and now the last piece of code, you make a while loop:
```python
while guesses < chances: # for a loop to happen, we need something to start it 
    guesses += 1
    guess = int(input("enter your guess: ")) # the first prompt 

    if guess == num: # and if its correct the code stops with a break 
        print(f'correct! the number is {num}. you guessed it in {guesses} attempts')
        break 
    elif guesses >= chances and guess != num: # if you dont have any guesses left ... 
        print(f'sorry, the number was {num}. better luck next time !!')
    elif guess > num: # the number you guessed was to high 
        print("to high !!")
    elif guess < num: # or the number you guessed to low
        print("to low !!")
```

now you´ve made a simple and easy guessing game, well done !! 


# hangman !

the game is a step up from the guessing game, and i have also added art to this project to make it better visually !! 

first add the art.py file into your folder, so you have the nessasary visuals. then you make the hangman.py.

(...)

```python
import random
from art import stages
```

add the wordlist (you can add a bigger wordlist if you pelase, but this is just and example):

```python
random_words = ["basketball", "football", "tennis", "badminton", "swimming", "track", "golf", "kayaking"]
```

now i randomise the word you will be guessing, and i also find out the word length so we can display how many letters the word has below:

```python
chosen_word = random.choice(random_words)
word_length = len(chosen_word)
```

now, i choose the variables for the lives you get (this is mathced with all the animations i have). 

```python
end_of_game = False
lives = 6
```



```python
display = []
for _ in range(word_length):
    display += "_"
```


```python
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
```

slow



(also credit to the user: hridaya423 (https://gist.github.com/hridaya423/ecbbe8651f61211bee11adc6de680ed6)for generall help with this code !!)

# snake

snake is one of the most popular arcade games and phone games, and we´r emaking it herere !! its an eazy tutorial on how to make it here yyuhhh:

