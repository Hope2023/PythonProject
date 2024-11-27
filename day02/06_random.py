import random
num=random.randint(1,10)
guess_num=int(input("Guess a number between 1 and 10: "))
if guess_num==num:
    print("Congrats! You guessed the number!")
    print("You win!")
else:
    if guess_num>num:
        print("Too high!")
    else:
        print("Too low!")

    guess_num=int(input("Guess a number between 1 and 10: "))
    if guess_num == num:
        print("Congrats! You guessed the number!")
        print("You win!")
    else:
        if guess_num > num:
            print("Too high!")
        else:
            print("Too low!")