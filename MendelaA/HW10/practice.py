
# class SSBird():
#     def __init__(self):
#         print("SSBird is ready")


class Bird:
    
    def __init__(self):
        print("Bird is ready")
 
    def whoisThis(self):
        print("Bird")
 
    def swim(self):
        print("Swim faster")
 
# child class
class Penguin(Bird):
 
    def __init__(self):
        # call super() function
        # Bird.__init__(self)
        super().__init__()
        print("Penguin is ready")
 
    def whoisThis(self):
        # Bird.whoisThis(self)
        super().whoisThis()
        print("Penguin")
        
 
    def run(self):
        print("Run faster")
 
peggy = Penguin()
peggy.whoisThis()
# peggy.swim()
# peggy.run()