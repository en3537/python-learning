import random

print("===================")

ans = random.randint(1, 9)

chance = 0

while True:
    chance+=1

    if (chance == 4):
        print("*** Failed: You have tried 3 time(s)!")
        print(f"*** Answer is {ans}!")
        break

    guess = int(input(f"Guess {chance}:"))

    if (guess == ans):
        print("*** Correct!")
        print("===================")
        print(f"*** Success: You have tried {chance} time(s)!")
        print(f"*** Answer is {ans}!")
        break
    elif (guess > ans):
        print("*** Incorrect: Smaller!")
        print("===================")
    else:
        print("*** Incorrect: Larger!")
        print("===================")