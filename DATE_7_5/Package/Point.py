class Point:
    count_of_instance = 0
    def set_x(self,x):
        self.x=x
    def get_x(self):
        return self.x
    def set_y(self,y):
        self.y=y
    def get_y(self):
        return self.y

    @staticmethod
    def static_method(self):
        return "static_method() 호출"

    @classmethod
    def class_method(cls):  # -> 클래스 참조를 위한 객체 참조값
        return "class_method() 호출"

def __init__(self, x=0, y=0):
    self.x, self.y = x, y
    Point.count_of_instance += 1
def __del__(self):
    Point.count_of_instance -= 1
def __str__(self):
    return "Point({0}, {1})".format(self.x, self.y)
def __repr__(self):
    return "\"Point({0}, {1})\"".format(self.x, self.y)
