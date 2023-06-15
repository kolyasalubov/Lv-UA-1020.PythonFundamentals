# Secret name
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


# Find the distance
def distance(x1, y1, x2, y2):
    find_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(find_distance, 2)


# No yelling!
def filter_words(st):
    return " ".join(st.capitalize().split())


# Convert a Number to a String!
def number_to_string(num):
    return str(num)


# Reversing Words in a String
def reverse(st):
    return " ".join(st.strip().split()[::-1])


# Reverse List Order
def reverse_list(l):
    l.reverse()
    return l


# Multiples of 3 or 5
def solution(number):
    new_list = []
    if number < 0:
        return 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            new_list.append(num)
    return sum(new_list)


# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    a = mpg * fuel_left
    if a < distance_to_pump:
        return False
    return True


# Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name.startswith("R", 0) or name.startswith("r", 0):
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


# Convert boolean values to strings 'Yes' or 'No'
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"


# Counting sheep...
def count_sheep(sheep):
    counter = 0
    for item in sheep:
        if item:
            counter += 1
    return counter


# Is this my tail?
def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    return False

