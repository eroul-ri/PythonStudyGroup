from study.Animal import Animal


class Dog(Animal):
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def cry(self):
        print('멍멍')