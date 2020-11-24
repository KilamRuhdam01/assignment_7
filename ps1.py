from random import randint
from math import log
from math import ceil
import sys
start = int(input("\nEnter the starting number : "))
end = int(input("\nEnter the ending number : "))

range_guess = end- start + 1
if range_guess<=0:
    print('\nEntered range is incorrect. Quitting now.')
    sys.exit()

num = randint(start,end)
num_of_guesses = ceil(log(range_guess,2))
#print (num)
print("\nGuess the number, you have {} guesses".format(str(num_of_guesses)))

while num_of_guesses:
    num_of_guesses-=1
    guess = int (input('\nEnter your guess : '))
    if guess == num:
        print('\nCongratulations! You are good at this guessing game. Your drinks are on the house\n')
        break
    elif guess < num and num_of_guesses:
        print("\nYour guess was low! Try again.")
        continue
    elif guess > num and num_of_guesses:
        print('\nYour guess was high! Try again.')
        continue
    else: 
        print('\nGame Over!!! You ran out of chances. The correct number was {}'.format(str(num)))
    