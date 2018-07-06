from Point import Point
def bound_class_method():
    p=Point()
    p.set_x(10)
    p.set_y(10)
    print(p.get_x(),p.get_y(),sep=',')
def unbound_class_method():
    p = Point()
    Point.set_x(p, 10)  # 객체를 첫 번째 인자에 할당하고 있음에 유의
    Point.set_y(p, 10)  # 객체를 첫 번째 인자에 할당하고 있음에 유의
    print(Point.get_x(p), Point.get_y(p), sep=',')
def main():
    bound_class_method()
    unbound_class_method()
def test_member():
    p = Point()
    Point.set_x(p, 10)
    Point.set_y(p, 10)
    print('x={0}, y={1}, count_of_instance={2}'.format(p.x, p.y, p.count_of_instance))
if __name__=='__main__':
    main()
def test_to_string():
    p = Point()
    print(p)
def test_to_string():
    p = Point()
    print(p)
    print(repr(p))
    p2 = eval(repr(p))
    print(p2)
