from utils import *
from models import *
print(dir())
print(list(filter(lambda str: not ("__" in str ), dir() )))