def birthday_info(year):
    try:
        if year % 2 != 0:
            raise Exception(f'{year} is not odd')
        elif year < 0:
            raise Exception('Not support negative numbre')
    except Exception as e:
        return e
    else:
        return f'{year} is odd'
    

print(birthday_info(-10))
print(birthday_info(5))
print(birthday_info(9))