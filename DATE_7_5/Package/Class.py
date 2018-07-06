def P_221():
    class MyString(str):
        pass

    s = MyString()
    print(type(s))
    print(MyString.__bases__)

    s2 = str()
    print(type(s2))
    print(str.__bases__)
