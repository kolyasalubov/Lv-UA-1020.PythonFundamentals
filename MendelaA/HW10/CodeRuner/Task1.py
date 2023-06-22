"""
Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
"""

class Ball():
    """
    Ball class
    """
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")

print(ball1.ball_type)
print(ball2.ball_type)
