from study.Country import Country


class USA(Country):
    def __init__(self, name, capital=None):
        self.name = name
        self.capital = capital
