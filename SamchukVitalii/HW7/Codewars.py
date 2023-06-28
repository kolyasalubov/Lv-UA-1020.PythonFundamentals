
def greet(name):

    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

########################

def distance(x1, y1, x2, y2):
    return round((((x2 - x1)**2 +(y2 - y1)**2)**0.5),2)

####################            
def filter_words(st):
    return " ".join(st.split()).capitalize()    

print(filter_words(input()))

######################

def number_to_string(num):
    return str(num)

###########################

def reverse(st):
    return " ".join(st.strip().split()[::-1])

def reverse_list(l):
    return l[::-1]

############################

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg * fuel_left:
        return True
    else:
        return False

############################

def are_you_playing_banjo(name):
    if name[0].lower()=='r' : 
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
#######################    

def bool_to_word(boolean):
    if boolean is True:
        return "Yes"
    elif boolean is False:
        return "No"
    
    
####################    
    
def count_sheeps(sheep):
    
    return sheep.count(True)
  # TODO May the force be with you

#####################3

def correct_tail(body, tail):

    #return tail == body[:-1]
    return body.endswith(tail)
    