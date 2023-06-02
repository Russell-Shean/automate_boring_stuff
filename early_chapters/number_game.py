import random
import sys

number = random.randint(1,20)
number_of_guesses = 0
guess = ''

numbers_as_string = []
for i in range(1,21):
  numbers_as_string.append(str(i))

while guess != number:
  print("\nI'm thinking of a number between 1 and 20")
  guess = input("Take a guess! ")
  
  if guess == "exit":
    sys.exit()
    
    
  if guess not in numbers_as_string:
    print("Sorry, that's not a number between 1 and 20. Please try again!")
    continue
    
  guess = int(guess)
    
  number_of_guesses = number_of_guesses + 1
  
  #print(number_of_guesses)

  if guess == number:
    print(f"Yay! You guessed the number in {number_of_guesses} guesses")
    
  elif guess > number:
    print("Your guess is too high :'( ")
    
  elif guess < number:
    print("Your guess is too low QQ")
    
