"""
Consider an array/list of sheep where some sheep may be missing from their place.
We need a function that counts the number of sheep present in the array (true means present).
"""

def count_sheeps(sheep):
    counter = 0
    for item in sheep:
        if item == True:
            counter += 1
    
    return counter


x = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

assert count_sheeps(x) == 17

"""
Solution from codewars
------------------------------------------------------------
def count_sheeps(herd):
  return sum(1 for sheep in herd if sheep)
------------------------------------------------------------
count_sheeps = lambda x: x.count(1)
------------------------------------------------------------
return sheep.count(True)
"""