def filter_words(st):
    for i in range(10, 1, -1):
        st = st.replace(' ' * i, ' ')
    if st[-1] == ' ':
        st = st[:-1]
    return st.capitalize()
