import os
if __name__ == '__main__':
    print("welcome to Robospeaker 1.1. Created by Affan")
    while True:
        x = input("what do you want to speak?")
        if x == "q":
            os.system("say 'bye bye friend")
            break
        command = f"say {x}"
        os.system(command)