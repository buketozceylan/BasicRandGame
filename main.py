import random
n = random. randint(0,10)

score = 100

Guess = int(input("Guess: "))

while n < 11:
    if Guess > n:
        print("Lower!")
        score -= 20
        print("Score: " + str(score))
        Guess = int(input("Guess: "))

    elif Guess < n:
        print("Higher!")
        score -= 20
        print("Score: " + str(score))
        Guess = int(input("Guess: "))

    elif (Guess == n) or (score <= 0):
        print("True. Number: " + str(n))
        print("Score: " + str(score))
        break
