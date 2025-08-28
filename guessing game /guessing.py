import random 

print("this is the number guessing game !! u get 10 chances to guess, for each guss it will get easier (i promise).")

low = int(input("now you have to choose in whatt range you want to guess the numbers, so enter the lowest range: "))
high = int(input("and now the highest number u want: "))

print(f'now you have 10 chances to guss the numbers from {low} to {high}, good luck !!')

num = random.randint(low,high)

chances = 10
guesses = 0

while guesses < chances:
    guesses += 1
    guess = int(input("enter your guess: "))

    if guess == num:
        print(f'correct! the number is {num}. you guessed it in {guesses} attempts')
        break 
    elif guesses >= chances and guess != num:
        print(f'sorry, the number was {num}. better luck next time !!')
    elif guess > num: 
        print("to high !!")
    elif guess < num: 
        print("to low !!")

