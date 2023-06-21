# 1
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)

#2
# import math
# def distance(x1, y1, x2, y2):
#     # Your code here
#     distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#     rounded_distance = round(distance, 2)
#     return rounded_distance

#3
# def filter_words(st):
#     words = st.split()
#     filtered_words = []
#     for i, word in enumerate(words):
#         if i == 0:
#             filtered_words.append(word.capitalize())
#         else:
#             filtered_words.append(word.lower())
#     filtered_sentence = ' '.join(filtered_words)
#     return filtered_sentence

#4
# def number_to_string(num):
#     return str(num)

#5
# def reverse(st):
#     words = st.split()
#     reversed_words = list(filter(lambda x: x.strip(), words))[::-1]
#     reversed_st = ' '.join(reversed_words)
#     return reversed_st

#6
# def reverse_list(l):
#     return l[::-1]

#7
# def solution(number):
#     if number <= 0:
#         return 0

#     multiples = [i for i in range(number) if i % 3 == 0 or i % 5 == 0]
#     return sum(multiples)

#8
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     fuel_consumption = 25
#     required_fuel = distance_to_pump / fuel_consumption

#     if fuel_left >= required_fuel:
#         return True
#     else:
#         return False

#9
# def are_you_playing_banjo(name):
#     if name[0] == "R" or name[0] == "r":
#         return name + " plays banjo"
#     return name + " does not play banjo"

#10
# def bool_to_word(boolean):
#     if boolean == True:
#         return str("Yes")
#     return str("No")

#11
# def count_sheeps(sheep):
#     count = 0
#     for is_present in sheep:
#         if is_present:
#             count += 1
#     return count

#12
# def correct_tail(body, tail):
#     if body[-1] == tail[0]:
#         return True
#     else:
#         return False
