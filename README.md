# pygames !!! 

ive made a lot of diffrenet pygames and eazy tutorials on how ot make and play them yeyy

her er en oversikt over alle tutorials:
- [pygames !!!](#pygames-)
  - [guessing game !](#guessing-game-)
  - [hangman !](#hangman-)  
  - [](#)  
  - [](#)


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

