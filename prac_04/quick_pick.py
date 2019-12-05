from random import randint

quick_pick_lines = int(input('How many quick picks? '))

for i in range(quick_pick_lines):
    one_line = []
    for j in range(6):
        number_to_append = randint(1, 45)
        while number_to_append in one_line:
            number_to_append = randint(1, 45)
        one_line.append(number_to_append)
    
    one_line.sort()
    for number in one_line:
        print('{:>2}'.format(number), end = ' ')
    
    print('\n')


