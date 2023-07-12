### Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

### Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
    s1 = x2 - x1
    s2 = y2 - y1
    dist = (s1 ** 2 + s2 ** 2) ** 0.5
    return round(dist, 2)

#### No yelling!
def filter_words(st):
    new_st = st.capitalize()
    final_st = " ".join(new_st.split())
    return final_st

####### Convert a Number to a String!
def number_to_string(num):
    this_str = str(num)
    return this_str

########## Reversing Words in a String
def reverse(st):
    st = st.split()
    st.reverse()
    st = " ".join(st)
    return st

########### Reverse List Order
def reverse_list(l):
    'return a list with the reverse order of l'
    l.reverse()
    return l

####### Multiples of 3 or 5
def solution(number):
    list1 = []
    if number < 0:
        return 0
    for  x in range (number):
        if x % 3 == 0 or x % 5 == 0:
            list1.append(x)
    return sum(list1)



############## Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    
    if fuel_left >= distance_to_pump / mpg:
        return True
    else:
        return False
    
############## Are You Playing Banjo?
def are_you_playing_banjo(name):
    
    
    if name.startswith("R") or name.startswith("r"):
    
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    

######## Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    
    if boolean == True:
        return "Yes"
    else:
        return "No"
    

############## Counting sheep...
def count_sheeps(sheep):
    num_of_sheep = 0
    for x in sheep:
        if x == False:
            pass
        elif x == True:
            num_of_sheep += 1
    return num_of_sheep

############### Is this my tail?
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False