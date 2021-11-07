import random
n = random. randint(0,10)

score = 100

Guess = int(input("Guess: "))

while n < 11:
    if Guess > n:
        print("Lower!")
        score = score - 10
        Guess = int(input("Guess: "))

    elif Guess < n:
        print("Higher!")
        score = score - 10
        Guess = int(input("Guess: "))

    elif Guess == n:
        print("True. Number: " + str(n))
        break
