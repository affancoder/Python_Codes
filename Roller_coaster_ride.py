print("To check wheter you are able to ride Roller Coaster or not?\n")
height = float(input("Input your height: "))

if height > 4.5:
    print("Congrats! you are able to ride Roller Coaster")
else:
    print("Sorry! you are not able to ride")

age = int(input("\ninput your age: "))
bill = 0
if age > 12:
    bill = 100
    print("Ticket price is $100")
elif age > 18:
    bill = 200
    print("Ticket price is $200")
elif age > 30:
    bill = 500
    print("Ticket price is $500")
elif age > 60:
    print("you are able to ride")
else:
    print("you are not allowed for ride")
    
photo = (input("Do you want to capture photos?(yes/no)\n"))
if photo == 'yes' or photo == 'Yes':
    bill = bill + 50
    print(f"Final price of your ticket is ${bill}")
else:
    print("ok")