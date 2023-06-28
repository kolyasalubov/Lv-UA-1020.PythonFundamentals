def God():
    return [man, woman]


class Human():
    def _init__(self):
        self.gender = None


class Man(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.gender = 'male'


class Woman(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.gender = 'female'


man = Man('Adam')
woman = Woman('Eve')
