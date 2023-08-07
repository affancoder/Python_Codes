#love calculator program
name1 = input("What is your name?\n")
name2 = input("What is your crush name?\n")
joint_string = name1 + name2
lower_case_string = joint_string

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
love = l + o + v + e
 
love_score = int(str(true) + str(love))

if love_score >= 3:
    print("You will polite to each other")
elif love_score >= 6:
    print("You will be happy with each other")
elif love_score >= 7:
    print("You will so much love to each other")
else:
    print("Good Frienship")