"""Write a generator function that returns all combinations of two lists.
"""
def combinations(list1, list2):
    for item1 in list1:
        for item2 in list2:
            yield item1, item2

            


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for combination in combinations(list1, list2):
    print(combination)
    