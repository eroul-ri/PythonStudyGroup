from study.Animal import Animal


class Monkey(Animal):
    def __init__(self, type, name, cry):
        self.type = type
        self.name = name
        self.cry = cry

    def show(self):
        super().show()
        print('type : ', self.type)
        print('name : ', self.name)
        print('cry : ', self.cry)