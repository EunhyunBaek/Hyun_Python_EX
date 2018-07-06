class Human:
    country='South Korea'
    def __init__(self,name):
        self.name=name

class BookReader(Human):
    def read_book(self):
        print(self.name+' is reading Book!')
class GuitarPlayer(Human):
    def play(self):
        print(self.name+ ' is playing Guitar!')

class Human:
    country='South Korea'
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name+' is eating')

class BookReader(Human):
    def read_book(self):
        print(self.name+' is reading Book!')
class GuitarPlayer(Human):
    def play(self):
        print(self.name+ ' is playing Guitar!')
class BookWriter(Human):
    def write_book(self):
        print(self.name+' is writing Book!')
#main

class Developer:
    def __init__(self,name):
        self.name=name
    def coding(self):
        print(self.name+ 'is developer')

class ProgramBookWriter(Human,Developer):
    def write_book(self):
        print(self.name+ 'ls writeing book')
class PythonDeveloper(Developer):
    def coding(self):
        print(self.name + 'is Python developer')
class JavaDeveloper(Developer):
    def coding(self):
        print(self.name + 'is Java developer')
class CppDeveloper(Developer):
    def coding(self):
        super().coding()
        print(self.name + 'is Cpp developer')

bw=BookWriter("Hyun")
bw.write_book()
bw.eat()

print(bw.__class__)
print(BookWriter.__class__)
print(BookWriter.__class__)
print(Human.__class__)
print(Human.__class__)

bz=ProgramBookWriter("hyun")
bz.write_book()
bz.eat()

ba=PythonDeveloper("hyun")
ba.coding()

ba=JavaDeveloper("hyun")
ba.coding()

ba=CppDeveloper("hyun")
ba.coding()