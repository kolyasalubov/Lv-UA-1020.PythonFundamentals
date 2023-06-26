class CustomError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)
    
#total_score = int(input("Enter expert score: "))
try:
    num_of_group = int(input("Enter number of your group: "))
    if num_of_group < 1:
        raise CustomError("Number of your group can't be less than 1")
except CustomError as e:
    print("We obtain error:", e.data) 