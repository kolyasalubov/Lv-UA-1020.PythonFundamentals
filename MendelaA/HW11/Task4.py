def days_num(num):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    try:
        if num not in range(1,8):
            raise Exception('Input error, shoud be from 1 to 7')
        else:
            return days[num-1]
    except Exception as e:
        return e
    

print(days_num(7))
print(days_num(1))
print(days_num(70))