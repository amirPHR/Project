import random 

while True:

    a = int(input('Choose:\n1.sang\n2.kaghaz\n3.gheichi\n4.Exit\n'))


    system = random.randint(1,3)
    system2 = ''

    if system == 1:
        system2 = 'sang'

    elif system == 2:
        system2 = 'kaghaz'
    
    elif system == 3:
        system2 = 'gheichi'

    if (system == 1 and a == 2) or (system == 2 and a == 3) or (system == 3 and a == 1):
        print('You are winner! ')

    elif a == system:
        print('Draw!') 
    
    elif a == 4:
        print('Exit...')
        break

    else:
        print('You are loos!')