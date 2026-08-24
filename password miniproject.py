# mini project
import time
unlocked = False
while True :
    no_of_attempts = 3
    while no_of_attempts >0:
        p=58734
        password = int(input("please enter your password : ",))
        if p==password :
            print("lock opened")
            unlocked = True
            break
        else :
            print("please enter correct password")
            no_of_attempts -=1
            if no_of_attempts==0:
                print('attempts locked,wait for 30 seconds')
                time.sleep(30)
    if unlocked :
        break