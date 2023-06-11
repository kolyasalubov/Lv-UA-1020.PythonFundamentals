def reverse(st):
    st = st.strip()
    st_list = st.split(" ")
    st = " ".join( reversed(st_list))
    return st
print(reverse("Helo wird"))