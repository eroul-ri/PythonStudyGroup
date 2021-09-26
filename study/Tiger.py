from sj.Animal import Animal


class Tiger(Animal):
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def cry(self):
        print('어흥')