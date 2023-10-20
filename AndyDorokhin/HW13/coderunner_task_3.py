""" 
    Write a generator function that returns all combinations of two lists.
    
    Examlpe:
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    Result:
    (1, 'a')
    (1, 'b')
    (1, 'c')
    (2, 'a')
    (2, 'b')
    (2, 'c')
    (3, 'a')
    (3, 'b')
    (3, 'c')
"""
def combinations(list1, list2):
    for x in list1:
        for y in list2:
            yield (x, y)


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for combination in combinations(list1, list2):
    print(combination)
