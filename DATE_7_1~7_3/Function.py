'''
함수:함수란
    입력값을 가지고 어떤 일을 수행한 다음 그 결과물을 내 놓는것

    함수를 사용하는 이유
        반복되는 부분이 있을 경우 재활용을 위해
        프로그램의 흐름을 일목요연하게 볼 수 있다.
함수 정의하기
    def 키워드를 이용하여 정의
    함수 이름과 인수들이 기술
    함수 선언부는 :로 끝난다
    들여쓰기 규칙이 허용
    함수의 끝은 들여쓰기가 적용 안되는 라인에서 끝난다.
함수도 객체다
    함수도 객체이므로 다음과 같은 호출도 가능하다.
    t=times
    print(t(100,100))
    print(t,times,sep=",")
함수:return
    함수를 종료시키고, 해당 함수를 호출한 곳으로 되돌아 가게 한다
    파이썬에서는 어떤 종류의 객체도 반환할 수 있다
    여러 객체를 return 하면 튜플로 반환한다
    return 문을 만나면 함수는 종료한다
    return문만 사용하면 None을 반환한다
    함수가 끝날 때 까지 종료할 필요가 없고 반환할 값이 없을 때는 return 문이 없어도 된다.
함수:인수의 전달 방법
    기본적으로 참조에 의한 호출(Call-by-reference)이다
    하지만 인수의 타입이 변경가능(mutable),변경불가(immutable)에 따라 처리 방식이 달라진다.
함수:스코핑 룰(Scope)
    이름공간(Namespace)
        프로그램에서 사용되는 이름들이 저장되는 공간
    이름은 값을 치환할 때 해당 값의 객체와 함께 생겨나고 이름 공간에 저장
    이름공간에 저장된 이름을 통해 객체를 참조
    이름공간의 종류
        Local Scope     :       함수내부
        Enclosed        :       function in function
        Global          :       모듈 내부
        Built-in        :       내장 영역
    동일한 이름이 여러 영역에 있다면 LEGB 순으로 찾는다.
함수:스코핑 룰 예제
    함수 내부에서 전역 객체를 사용해야 하는 경우 global 선언문을 이용한다
    가능하면 함수 내부에서 글로벌 객체를 직접 사용하는 것은 피한다.
함수:함수의 인수
    인수는 필요한 개수만큼 선언할 수 있다.
    기본값이 필요하면 함수 선언시 지정 할 수 있다.
함수:함수의 인수 - 키워드 인수
    인수값을 인수 이름으로 전달할 수 있다(함수의 정의에 따른다.)
함수:함수의 인수 - 가변인수
    정해지지 않은 개수의 인수값을 받을 때 사용한다
    선언시 인수명 앞에 *를 붙여 선언한다.
함수:함수의 인수 - 사전 키워드 전달
    정해지지 않은 키워드 인수는 모두 dict로 받을 수 있다
    선언시 인수명 앞에 **를 붙인다
    사전 키워드 인수는 선언의 맨 마지막에 있어야 한다
함수:함수 객체를 인수로 전달
    파이썬에서는 함수도 객체이다
    따라서 인수로 함수를 전달하는 것도 가능하다.
함수:익명 함수(Lambda)
    이름이 정의되지 않은 '익명 함수'를 선언
    데이터 분석/변형 함수에서 파라미터로 처리 함수를 인자로 받는 경우가 많다
함수:lambda를 이용한 정렬
    정렬할 때, key 함수로 정의하기에도 편리한 경우가 많다.
'''
#########################################################################
#Global
x=1
g=1
#########################################################################
#function
def dummy():
    pass
def my_function():
    print("Hello World")
def times(a,b):
    return a*b
def do_nothing():
    return #return 문만 썻을 경우, Nome 이 반환
def say_hello():
    print("Life is too short, You need Python")

def max_value(a,b):
    if a>b:
        return a
    else:
        return b
def swap(a,b):
    return b,a
def g(t):
    t[0]=0
def h(t):
    t=(10,20,30)
def func(a):
    return a+x
def func2(a):
    x=2
    return a+x
def func3(a):
    global g #global 에 존재 하는 것 사용
    g=3
    return a+g
def sum(a,b):
    return a+b
def incr(a,step=1):#두 번째 인자의 기본값은 1
    return a+step
def area(width,height):
    return width *height
def get_total(*args):
    sum=0
    for x in args:
        sum +=x
    return sum
def get_total2(*args):
    sum = 0
    #list 인자값 받아서 정수형으로 더할 수 있도록 해결하기
    for x in args:
            sum += x
    return sum
def f(a,b,*args,**kwd):
    print(a,b)
    print(args)
    print(kwd)
def clean_strings(strings, *funcs): # 함수 목록을 가변인수로 전달
    results = []
    for string in strings:
        for func in funcs: # 전달된 함수들을 순차적으로 적용
            string = func(string)
        results.append(string)
    return results
def square(x):
    return x*2

#########################################################################
#main
dummy()
my_function()
print(times(10,10))
print(do_nothing())

t = times
print(t(100, 100))
print(t, times, sep=",")
print(swap(10,20))#결과값은 튜플로 반환된다.
a=[1,2,3]
g(a)
print(a)
a=(1,2,3)
print(a)

print(func(10))
print(func2(10))
print(x)

print(func3(10))
print(g)

print(sum(2,3))
print(incr(10))
print(incr(10,2))

print(area(10,12))
print(area(height=4,width=3))#==area(3,4)

print(get_total(1,3,5,7,9))
#print("total2")
#print(get_total(range(0,100,2)))
print("ffffffffff")
f(10,20,30,40,depth= 10,dimension=3,hell=4)

states = ['Alabama', ' Georgia', 'Georgia ', 'georgia', 'FlOrIda',
'south carolina ', 'West virginia']
states = clean_strings(states, str.strip, str.title)
print(states)

for i in range(10):
    print("{0}:{1}".format(i, square(i)), end = " ")
else:
    print()
# Same as above with Lambda
for i in range(10):
    print("{0}:{1}".format(i, (lambda x: x * 2)(i)), end = " ")
else:
    print()

strings = ['foo', 'card', 'bar', 'abab', 'aaaa', 'abab', 'foo']
strings.sort(key=lambda x: len(x))
print(strings)
strings.sort(key=lambda x: strings.count(x))
print(strings)