day = input('Enter weekday number: ')
weekdays = ('Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday')

try:
    day_num = int(day)
    print(f'{day_num} is {weekdays[day_num - 1]}')
except:
    print('Error: day number must be an integer in range 1 to 7')
