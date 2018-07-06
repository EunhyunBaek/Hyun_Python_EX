"""
class BookReader:
    name=str()
    #read_book():
    print(name+' is reading Book!')

reader = BookReader()
type(reader)
reader.name='pmk'
reader.read_book()
dir(BookReader) #_BookReader__country
"""



class BookReader:
    __country = 'South Korea'  # 클래스 변수
    name=str()

    #def read_book(self):

class BookReader:
    country = 'South Korea'
    name = str()
    def read_book(self):
        print(self.name+' is reading Book!')

    dir(BookReader)

class BookReader:
    country = 'South Korea'
    def __init__(self,name):# 클래스 변수
        self.name=name
    def read_book(self):
        print(self.name + ' is reading Book!')
    dir(BookReader)
class BookReadr:
    __country = 'South Korea'
    def set_country(self,country):
        self.__country=country
    def get_country(self,country):
        self.__country=country
def VAR():
    var = '파이선 프로그래밍'
    print(id(var))
    print(type(var))
    str
    print(type(str))
    print(type(type))
    print(id(str))

    var.__class__
    var.replace('파이썬', 'Python')
    print(var)
#main
VAR()
#reader=BookReader()# error 필수인자 누락
#reader.name='back'
#reader.read_book()

reader1 = BookReader('Hyun')
reader2 = BookReader('Eun')
reader1.country
reader2.country
reader1.read_book()
reader2.read_book()
