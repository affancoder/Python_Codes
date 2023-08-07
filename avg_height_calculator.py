#Average height calculator 
heights = (input("Enter all heights in cm: "))
h_list = heights.split()
print(h_list)
count = 0
for heights in h_list:
    count = count+1
print(f"{count} is total no of heights entered")
for i in range(count):
    h_list[i]= int(h_list[i])
print(h_list)
sum = 0 
for person in h_list:
    sum = sum + person
avg = sum/count
print(f"{avg}cm is the average height")