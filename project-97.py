import random
num = random.randint(1, 9)
chance = 4
while chance > 0:
    guess = int(input("Enter your guess:- "))
    if(guess == num):
        print("YOU WON!!! your guess was correct")
        break
    elif(guess > num):
        print("Your guess was too high, guess a number lower than", guess)
    elif(guess < num):
        print("your guess was too low, guess a number higher than", guess)
    chance = chance - 1

if(chance == 0):
    print("YOU LOSE!!! The number is", num)