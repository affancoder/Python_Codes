first = input("Enter any first number: ")
operator = input("Enter any operator(+,-,*,/,%): ")
second = input("Enter any second number: ")

if operator =="+" :
    print(int(first) + int(second))

elif operator =="-":
    print(int(first) - int(second))

elif operator =="*":
    print(int(first) * int(second))
    
elif operator =="/":
    print(int(first) / int(second))

elif operator =="%":
    print(int(first) % int(second))

else:
    print("invalid operation")