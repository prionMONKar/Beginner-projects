import time

def countdown(getUserInput):
    while getUserInput:
        min, secs = divmod(getUserInput, 60)         #divmod function is used to convert seconds to minutes and seconds.
        timer = '{:02d}:{:02d}'.format(min, secs-1)  #formatting the time
        print(timer, end='\r')                       #Overwrite the line after each second
        time.sleep(1)                                #pausing the loop for one second
        getUserInput-=1                              #reducing time by 1 for each second pass
    print(timer)
    print("Fire!! Fire!! Firee!!")

getUserInput = int(input("Please enter the time to coundown in seconds: "))  

countdown(getUserInput)                              #Call the function
