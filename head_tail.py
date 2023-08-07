import random 
print("Press 0 for head & Press 1 for tail")
coin = int(input("Which side will you choose of coin?\n"))

a = random.randint(0,1)
if a == 0:
    print("Head")
else:
    print("Tail")