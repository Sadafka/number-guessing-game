import random

print('------Welcome to the number guessing game------ ')
number = random.randint(1, 100)

attempt = 0

while True:
    guess = int(input('Guess a number between 1 to 100'))
    attempt += 1
    
    if guess < number:
        print('Too low! Try a higher number.')
    elif guess > number:
        print('Too high! Try a lower number.')
    else:
        print(f'Congratulations! your guessed it in {attempt} attempts.')
        break