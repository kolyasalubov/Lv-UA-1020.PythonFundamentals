## 1. Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"



## 2. Simple: Find The Distance Between Two Points
## Це моє рішення не пройшло всі додаткові тести, але пройшло основні. 
## Не змогла розібратись чому

# from math import sqrt

# def distance(x1, y1, x2, y2):  
#     a = x2-x1
#     b = y2-y2       
#     gip = round(sqrt(a**2 + b**2), 2)
#     return gip



## 3. No yelling!

# def filter_words(st):
#     norm = st.capitalize()
#     norm2 =' '.join(norm.split())
#     return norm2


## 4. Convert a Number to a String!

# def number_to_string(num):
#     s = str(num)
#     return s


## 5. Reversing Words in a String

# def reverse(st):
#     list1 = st.split()
#     list2 = list1[::-1]
#     st_rev = ' '.join(map(str, list2))
    
#     return st_rev


## 6. Reverse List Order

# def reverse_list(l):
#     l2 = l[::-1]
#     return l2


## 7. Multiples of 3 or 5

# def solution(number):
#     sum = 0
#     if number <= 0:
#         return 0
#     else:
#         for s in range(number):
#             if s%3 == 0 or s%5 == 0:
#                 sum +=s
#     return sum


## 8. Will you make it?

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if mpg*fuel_left >= distance_to_pump:
#         return True
#     return False


## 9. Are You Playing Banjo?

# def are_you_playing_banjo(name):
#     name2 = name.lower()
#     if name2[0] == "r":
#         return name + " plays banjo"
#     return name + " does not play banjo"


## 10. Convert boolean values to strings 'Yes' or 'No'.

# def bool_to_word(boolean):
#     if boolean:
#         return "Yes"
#     return "No"


## 11. Counting sheep...

# def count_sheeps(sheep):
#     counter = 0
#     for c in sheep:
#         if c:
#             counter +=1
#     return counter


## 12. Is this my tail?

# def correct_tail(body, tail):
#     if body[-1] == tail:
#         return True
#     return False

