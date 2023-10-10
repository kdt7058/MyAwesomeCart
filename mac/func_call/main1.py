class ABC2:
    def __init__(self, input_config):
        self.conf = input_config

    def func2(self):
        print("First Name: ", self.conf.f_name)
        print("Last Name: ",  self.conf.l_name)
        print("Age: ", self.conf.age)

# if __name__ == '__main__':


