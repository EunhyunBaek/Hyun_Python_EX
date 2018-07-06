'''
튜플(Tuple)
    리스트와 거의 비슷하지만 다름: 시퀀스 자료형
        튜플은 () 기호로 생성하며 그 값을 바꿀 수 없다(immutable)
        하나의 요소만을 가질 때는 요소 뒤에 컴마(,)를 반드시 붙임
        괄호를 생략해도 튜플로 인식

    Packing과 UnPacking
        Packing:        나열된 객체를 Tuble로 저장하는것
        UnPacking:      튜플,리스트 안의 객체를 변수로 할당하는 것
    expansion(확장) unpacking
        Unpacking 시 왼쪽 변수가 부족한 경우, 에러가 발생한다(ValueError)
        확장 Unpacking에서는 왼쪽 변수가 적은 경우에도 적용할 수 있다(*)

'''

######################################################################################
#function

def Tuple(t):
    print(Tuple)
    print(t,type(t))                        #class = tuple

def Tuple2(t):
    print(Tuple2)
    print(t[-2],t[-1],t[0],t[1],t[2])       #인덱싱
    print(t[:])

    print(t*2)                              #반복 (*)
    print(t+(3,4,5))                        #연결 (+)
    print(len(t))                           #요소 개순 반환
    print(5 in t)                           #요소 5가 내부에 있는지 확인

def Tuple_Packing_UnPacking(t):
    print(Tuple_Packing_UnPacking)
    print(t,type(t))

    #unpacking tuple
    a,b,c,d=t
    print(a,b,c,d)

    #unpacking list
    a,b,c,d = [10,20,30,'python']
    print(a,b,c,d)

def ExpansionUnPacking(t):
    print(ExpansionUnPacking)
    # a,b=(10,20,30,40,50)#Value Error 발생
    # *가 존재할 경우 나머지 변수에 값을 넣고 난 후 나머지를 전부 *변수에 넣게 된다.

    #unpacking
    a, *b = t           # a=1                b=[2,3,4,5,6]
    *c, d = t           # c=[1,2,3,4,5]      d=6
    e, f, *g = t        # e=1                f=2                 g=[3,4,5,6]
    i, *j, k = t        # i=1                j=[2,3,4,5]         k=6

    print("t")
    print(t)
    print("a,*b")
    print(a,b)
    print("*c,d")
    print(c,d)
    print("e,f,*g")
    print(e,f,g)
    print("i,*j,k")
    print(i,j,k)
######################################################################################
#main
t=(1,2,3)
Tuple(t)

t=1,2,'python'#()를 생략해도 튜플을 생설 할 수 있다.
Tuple2(t)

#packing
t=10,20,30,'python'
Tuple_Packing_UnPacking(t)

t=1,2,3,4,5,6
ExpansionUnPacking(t)

