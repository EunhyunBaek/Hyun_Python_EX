'''
객체:심볼테이블
    변수의 이름과 저장된 데이터의 주소를 저장하는 테이블
    심볼테이블의 내용을 살펴보기 위해 globals(),locals() 내장 함수를 이용
    두 함수는 해당 스코프 내 심볼 테이블의 내용을 dict 타입의 객채로 반환한다.

객체:레퍼런스 카운트와 쓰레기 수집
    레퍼런스 카운트(Reference Count): 객체를 참조하는 참조 수
    레퍼런스 카운트가 0이 되면 사용하지 않는 객체로 판단, 자동으로 사라짐
    이러한 작업을 쓰레기 수집(Garbage Collection)이라함

객체:객체 ID
    id() 함수를 이용하면 객체의 주소를 식별할 수 있다.
        만일 두 객체의 ID가 동일하면, 같은 객체를 참조하고 있는 것

객체: 레퍼런스 복사
    객체를 참조하는 주소만 복사하는 것
객체: 객체의 복사
    [:] 이용한 복사
        객체 전체를 가르키는 [:]를 이용하여 복사한다.
    copy 함수 이용
        copy 모듈의 copy 함수를 사용하여 복사한다.
    deepcopy 함수 이용
        copy 모듈의 deepcopy 함수를 사용하여 복사한다.
        deepcopy는 복합객체를 재귀적으로 생성하고 복사한다.
'''
import sys
import copy
g_a=1
g_b="symbol"
##################################################################################
#function
def Local():
    print(Local)
    l_a=2
    l_b="table"
    print(locals())

def Global():
    print(Global)
    print(globals())

def SYS():
    print(SYS)
    x=object()
    print(sys.getrefcount(x))
    print(sys.getrefcount(x))
    print(sys.getrefcount(x))
    print(sys.getrefcount(x))
    y=x
    print(sys.getrefcount(x))
    print(sys.getrefcount(y))
    del(x)
    print(sys.getrefcount(y))
def FINDID():
    i1=10
    i2=10
    print(hex(id(i1)),hex(id(i2)))
    l1=[1,2,3]
    l2=[1,2,3]
    print(hex(id(l1)), hex(id(l2)))
    s1="hello"
    s2="hello"
    print(hex(id(s1)), hex(id(s2)))
    print(i1 is i2)
    print(l1 is l2)
    print(s1 is s2)
def Reference_Copy():
    print(Reference_Copy)
    x=[1,2,3]
    y=x
    print(y)
    print(hex(id(x)), hex(id(y)))
    x[1]=4
    print(y)

    x=[1,2,3]
    y=x[:]
    print(y)
    print(x is y)

    x[1]=4
    print(y)

    x=[1,2,3]
    y=copy.copy(x)
    print(x is y)
    x[1]=4
    print(y)

    a=[1,2,3]
    b=[4,5,a]
    x=[a,b,100]
    #얕은복사 shallow copy
    y=x
    print(id(y))

    #깊은복사 deep copy
    y=copy.deepcopy(x)
    print(id(y))
    a[2]=4
    print(id(y))
###################################################################################
#main
Local()
Global()
SYS()
FINDID()
Reference_Copy()