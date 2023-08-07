import random
user = int(input("Enter any number: "))

computer = random.randint(0,10)
while(1):
    if user == computer:
        print("Correct guess")
        break;
    elif user < 5:
        print("You guessing very less")
        break;
    elif user > 10:
        print("You are guessing big number")
        break;
    else:
        print("out of range")
        break;