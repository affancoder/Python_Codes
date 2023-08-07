#Know your BMI
weight = (input("Enter your weight in kg: "))
height = (input("Enter your height in meter: "))

BMI = int(weight)/float(height)**2
print("\nYour BMI is: ")
print(int(BMI))

print("\nHealthy BMI is considered between 18 to 25")

if int(weight)>18:
    print("You are underweight")
    
    
elif(int(weight)>=18 and int(weight)<=25):
    print("Congratulations! You are fit")
    
elif int(weight)>26:
    print("You are over weight")
   
    
else:
    print("invalid")
    