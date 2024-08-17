import random 

while True:
    inp = int(input('Choose a number between 1,100:\n'))

    system = random.randint(1,10)

    #commands
    if inp == system:
        print('You are winner!')
        break

    else:
        print('You are looser!')