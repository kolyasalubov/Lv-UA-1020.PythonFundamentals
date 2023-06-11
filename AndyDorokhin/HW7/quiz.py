def rec(in_param):
    if in_param<5:
        print(in_param)
        rec(in_param + 1)
        print(in_param)
rec(1)

def output_param(x, y , z):
    print(x, y, z)

my_type = (1, 2, 3)
output_param(*my_type)

my_fucn = lambda x : x if x > 5 else x**2 * my_fucn(10)
print(my_fucn(2))
