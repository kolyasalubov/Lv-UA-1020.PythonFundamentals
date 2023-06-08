def filter_words(st):
    word_list = st.lower().capitalize().split()
    return ' '.join(word_list)
print (filter_words('hELLO      world!,   my fRiend  '))