#Calculating BMI
weight = input("Input your weight in kg: ")
height = input("Input your height in meter: ")

BMI = round(int(weight)/float(height)**2)
print("\n")
if BMI<18:
    print(f"Your BMI is {BMI} and you are underweight")
    
elif BMI<25:
    print(f"Your BMI is {BMI} and Congrats! you are in healthy weight")
    
elif BMI<29:
    print(f"Your BMI is {BMI} and you are obese")

elif BMI<35:
    print(f"Your BMI is {BMI} and you are obese I")

else:
    print(f"Your BMI is {BMI} and you are obese I")
print("--------------------------------")