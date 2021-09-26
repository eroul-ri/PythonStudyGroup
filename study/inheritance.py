from study.Dog import Dog
from study.Korea import Korea
from study.Tiger import Tiger
from study.USA import USA

korea = Korea('한국', '서울', ['경상도', '전라도', '강원도'])
# korea2 = Korea('한국2', '서울2')
usa = USA('미국', '워싱턴')

korea.show()

tiger = Tiger('미미', '호랑이')
tiger.cry()

dog = Dog('홍시', '개')
dog.cry()