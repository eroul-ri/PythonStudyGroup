# 상속 inheritance
# sub Class
from study.Province import Province
from study.Country import Country


class Korea(Country, Province):
    def __init__(self, name, capital, provinceList):
        self.name = name
        self.capital = capital
        self.provinceList = provinceList
        # if population is not None:
        #     self.population = population

    # 부모 메서드 오버라이딩
    def show(self):
        super().show()
        # print(super().name)
        print('name : ', self.name)
        print('capital : ', self.capital)
        print('population : ', self.population)
        print('provinceList : ', self.provinceList)

    def show_korea(self):
        print('국가이름 : ', self.name)
