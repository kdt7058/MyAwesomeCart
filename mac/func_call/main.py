from main1 import ABC2


class ABC1:

    def __init__(self):
        self.f_name = 'Krihsna'
        self.l_name = 'Tapse'
        self.age = 25


if __name__ == '__main__':
    # create object
    obj1 = ABC1()

    obj2 = ABC2(obj1)
    obj2.func2()
