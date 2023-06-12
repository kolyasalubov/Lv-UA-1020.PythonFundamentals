from util import calc_rec, calc_tri, calc_circle

choice = input('Chose shape (1 - rectangle, 2 - triangle, 3 - circle): ')

match choice:
    case '1':
        calc_rec()
    case '2':
        calc_tri()
    case '3':
        calc_circle()
    case _:
        print('Error: incorrect input. Restart the program')
