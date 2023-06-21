# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

# class Ball():
#     def __init__(self, ball_type = "regular"):
#         self.ball_type = ball_type
#
# ball1 = Ball()
# ball2 = Ball("super")
# print(ball1.ball_type)
# print(ball2.ball_type)

####################################################################################################
# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# # Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
# import random
# class Ghost():
#     x = ["white", "yellow", "purple", "red"]
#     def __init__(self):
#         self.color = random.choice(self.x)
#
# ghost = Ghost()
# print(ghost.color)
##################################################################################################
# You have to do God's job. The creation method must return an array of length 2 containing objects
# (representing Adam and Eve). The first object in the array should be an instance of the class Man.
# The second should be an instance of the class Woman. Both objects have to be subclasses of Human.
# Your job is to implement the Human, Man and Woman classes.

# class Human:
#     pass
# class Man(Human):
#     pass
# class Woman(Human):
#     pass
#
# def God():
#     Adam = Man()
#     Eve = Woman()
#     return [Adam, Eve]
