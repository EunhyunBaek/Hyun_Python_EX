from Point import Point
def bound_class_method():
    p=Point()
    p.set_x(10)
    p.set_y(10)
    print(p.get_x(),p.get_y(),sep=',')

def main():
    bound_class_method()


if __name__=='__main__':
    main()