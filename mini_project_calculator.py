first = input("Enter first number: ")
operator = input ("Enter any operator (+,-,*,/,%): ")
second = input("Enter second number: ")
#int is declaration that first and second is integers to be add this is not string
int(first)
int(second)
if operator == "+":
    print(first + second)

elif operator =="-":
    print(first - second)

elif operator =="*":
    print(first * second)
    
elif operator == "/":
    print (first/second)

elif operator =="%":
    print(first%second)
    
else:
    print("invaild operation")