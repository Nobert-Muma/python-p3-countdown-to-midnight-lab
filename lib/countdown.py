# your code goes here!
import time
def countdown(number):
    count=number
    while count>=1:
        print(f'{count} SECOND(S)!')
        count-=1
    print("HAPPY NEW YEAR!")
def countdown_with_sleep(integer):
    count=integer
    while count>=1:
        print(f"{count} SECOND(S)!")
        count-=1
        time.sleep(1)
    print("HAPPY NEW YEAR!")
countdown(12)
countdown_with_sleep(10)