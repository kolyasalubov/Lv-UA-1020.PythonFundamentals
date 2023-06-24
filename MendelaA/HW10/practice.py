
# # class SSBird():
# #     def __init__(self):
# #         print("SSBird is ready")


# class Bird:
    
#     def __init__(self):
#         print("Bird is ready")
 
#     def whoisThis(self):
#         print("Bird")
 
#     def swim(self):
#         print("Swim faster")
 
# # child class
# class Penguin(Bird):
 
#     def __init__(self):
#         # call super() function
#         # Bird.__init__(self)
#         super().__init__()
#         print("Penguin is ready")
 
#     def whoisThis(self):
#         # Bird.whoisThis(self)
#         super().whoisThis()
#         print("Penguin")
        
 
#     def run(self):
#         print("Run faster")
 
# peggy = Penguin()
# peggy.whoisThis()
# # peggy.swim()
# # peggy.run()


class Account(object):
    counter = 0
    def __init__(self, holder, number, balance,credit_line=1500):
        Account.counter += 1
        self.__Holder = holder
        self.__Number = number
        self.__Balance = balance
        self.__CreditLine = credit_line
    
    def __del__(self):
        Account.counter -= 1

print(Account.counter)
a1 = Account("Homer Simpson", 2893002, 2325.21)
print(Account.counter)