#greeting according to time
import time

while True:
    timestamp = time.strftime("%H.%M.%S")
    hour = int(input("enter hour: "))
    print(hour)

    if (hour > 0 and hour < 11):
        print("Good Morning")
    elif(hour > 12 and hour < 16):
        print("good afternoon")
    elif(hour > 17 and hour < 20):
        print("good evening")
    else:
        print("good night")
    n = int(input("next: "))
    if n==0:
        break