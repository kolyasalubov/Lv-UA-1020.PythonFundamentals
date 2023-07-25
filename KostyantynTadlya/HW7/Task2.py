import areas

figure = input('Input the figure name ')

match figure:
    case 'triangle':
        h = float(input('Enter the heght of triangle '))
        a = float(input('Enter the base of triangle '))
        print(areas.area_of_triangle(h, a))
    case 'rectangle':
        a = float(input('Enter the side of rectangle '))
        b = float(input('Enter the other side of rectangle '))
        print(areas.area_of_rectangle(a, b))
    case 'circle':
        r = float(input('Enter the radius of circle '))
        print(areas.area_of_circle(r))