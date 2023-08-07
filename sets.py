set1 = {"Affan","Akash","Rahul"}
set2 = {"Vivek","Rohan","Shib","Khan"}
set3 = {"Khan","Atif","Harry"}
set4 = {"Peter","John"}
print(type(set2))
print("\n")
print(set1.union(set2))
print("\n" )
print(set1 | set2 | set3 | set4)
print("\n")
print(set1.union(("Sheikh","Aslam")))
print(set1.intersection(set2,set3))
print(set2.update(set3))