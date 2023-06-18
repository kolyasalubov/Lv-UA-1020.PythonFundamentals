# Jenny's secret message

def greet(name):
    return "Hello, my love!" if name == "Johnny" else  f"Hello, {name}!"



# Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(distance, 2)


# No yelling!
def filter_words(st):
    x = ' '.join(st.split())
    return x.capitalize()

# Convert a Number to a String!
def number_to_string(num):
    return str(num)


# Reversing Words in a String
def reverse(st):
    list = st.split()
    new_list = list[::-1]
    result = " ".join(new_list)
    return result

def reverse(st):
    return " ".join(reversed(st.split())).strip()


def reverse(st):
    list = st.split()
    new_list = list[::-1]
    result = ""
    for item in new_list:
        result += item
        result += " "
    return result

# Reverse List Order
def reverse_list(l):
    return l[::-1]

def reverse_list(l):
    l.reverse()
    return l


# Multiples of 3 or 5

def solution(number):
    if number < 0:
        return 0
    sum = 0
    for item in range(number):
        if item % 3 == 0 or item % 5 == 0:
            sum += item
    return sum


# Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left * mpg >= distance_to_pump:
        return True
    else:
        return False

def zeroo_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump


#Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return "Yes" if boolean == True else "No"


#Counting sheep...

def count_sheeps(sheep):
    count = 0
    for item in sheep:
        if item == True:
            count += 1
    return count

# Is this my tail?

def correct_tail(body, tail):
    return True if body[-1].lower() == tail[0].lower() else False