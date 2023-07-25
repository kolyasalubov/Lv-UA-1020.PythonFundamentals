class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)
        self.info = f"{self.name}s age is {self.age}"

    def getInfo(self):
        return self.info
