"""
Write a function taking in a string like WOW this is REALLY          amazing
and returning Wow this is really amazing. String should be capitalized and properly spaced.
Using re and string is not allowed.
"""
def filter_words(st:str):
    st = st.lower().capitalize().split()
    return ' '.join(st)
    
print(filter_words('WOW this is REALLY          amazing'))