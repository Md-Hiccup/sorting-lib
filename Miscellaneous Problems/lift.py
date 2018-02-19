# Lift Problem 

import random   

def elevator():
    choice = 0
    floor = random.randrange(10)
    print('The elevator is now on floor',floor)
    print('On which floor you are at ')
    choice = int(input())    
    chk(choice, floor)
    floor = choice
    print('To which floor you want to go')
    choice1 = int(input())
    chk(choice1, floor)

def chk(choice, floor):
    if( choice < floor):
        goDown(floor, choice)
    elif( choice > floor):
        goUp(floor, choice)
    elif(choice == floor):
        print('Enter the lift')
        

def goDown( floor, choice):
    print('The elevator is on its way down..')
    for i in range(floor, choice-1, -1):
        print(i, end=' ')
    
    print('\nThe elevator has arrived')
    
def goUp(floor, choice):
    print('The elevator is on its way up..')
    for i in range(floor, choice+1, 1):
        print(i, end=' ')
    print('\nThe elevator has arrived')

elevator()
