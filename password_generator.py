# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
print("Welcome to password generator!\n")
letters = ['a','b','c','d','e','A','B','C','D','E']
symbols = ['@','#','%','$','&','*','?']
numbers = ['1','2','3','4','5']
n=1
while True :
    n_letters = int(input("How many letters you want in your password ?\n"))
    n_symbols = int(input("how many symbols you want in your password ?\n"))
    n_numbers = int(input("How many numbers you want to add?\n" ))
    password=""
    for i in range(1,n_letters+1):
        char = random.choice(letters)
        password = password + char
    for i in range(1,n_symbols+1):
        char = random.choice(symbols)
        password = password + char
    for i in range(1,n_numbers+1):
        char = random.choice(numbers)
        password = password + char
    print(f"\nYour strong password is {password}")
    print("\nTo continue press 1 or to exit press 0")
    n=int(input())
    if n==0:
        break