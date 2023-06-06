def filter_words(st):
    word_list = st.lower().capitalize().split()
    return ' '.join(word_list)
print (filter_words('hELLO      world!,   my fRiend  '))

def loop_realization_of_filters (st):
    st_rep = st
    for item in range(len(st)-1):
        if st[item] ==" ":
          st_rep = st_rep.replace(" ", "")
    return 

        
print()