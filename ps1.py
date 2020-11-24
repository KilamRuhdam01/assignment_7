from random import randint
from math import log
from math import ceil
start = int(input("\nEnter the starting number : "))
end = int(input("\nEnter the ending number : "))

range_guess = end- start + 1

num = randint(start,end)
num_of_guesses = ceil(log(range_guess,2))
#print (num)
print("\nGuess the number, you have {} guesses".format(str(num_of_guesses)))

#while num_of_guesses:
 #   guess = int (input('\nEnter your guess'))