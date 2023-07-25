word = input("Enter any word :")

def number_of_characters(word):
    result_dict = {}
    for x in word:
        num_of_char = word.count(x)
        result_dict.update({x : num_of_char})
        
    return result_dict
    
print(number_of_characters(word))