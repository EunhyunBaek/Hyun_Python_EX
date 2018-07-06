'''
조건문
    조건표현식(Conditional Expression)
        C 또는 Java 의 3항 연산자와 같은 역활을 한다.
        value={true-expr}if{condition} else {false-expr}
    in,not in
        파이썬은 리스트,튜플,문자열에 in,not in 등 편리한 조건식을 제공
    in                         not in
    x in 리스트                x not in 리스트
    x in 튜플                  x not in 튜플
    x in 문자열                x not in 문자열

반복문:for
    {객체}는 list,str,tuple,bytes,bytearray,range 등 시퀸스 자료형
    반복횟수는 {객체}의 크기
    {객체}안의 객체를 하나씩 순차적으로 꺼내어 구문1,2가 실행됨
    반복이 정상적으로 끝나면 else 블록이 실행
    for문 내에서 break로 빠져나오면 else 블록은 실행되지 않음

반복문:enumerate
    요소의 값은 물론 인덱스가 필요할 경우 enumerate() 함수를 이용한다.

반복문:break
    어떤 조건에서 반복을 중지하고 빠져나가야 하는 경우 break문

반복문:continue
    Continue문읆 ㅏㄴ나면, 이후 구문은 실행하지 않고 처음으로 이동한다.

반복문:while
    {조건}이 참인 동안 구문1,2가 반복 실행
    else 블록은 while문을 빠져나올 때 실행
    단, break로 while문을 빠져나올 경우 else 블록은 실행되지 않는다.
    무한루프(실행이 종료되지 않고 계속 실행되는 반복)에 빠지지 않도록 유의
    경우에 따라서는 의도적으로 무한루프를 돌리기도 한다.

반복문:list
    리스트 내포(List Comprehension)를 이용하면 좀더 직관적인 프로그램을 만들 수 있다.
    [{표현식} for {항목} in {객체} if {조건}]
'''
######################################################################################
#function
def IF_ELIF_ELSE(n):
    print(IF_ELIF_ELSE)
    if n>0:
        print("양수")
    elif n<0:
        print("음수")
    else:
        print("0")

def Conditional_Expression(m):
    print(Conditional_Expression)
    print("by taxi" if m > 10000 else "by bus")

def IN_NOTIN():
    print(IN_NOTIN)
    print(1 in [1,2,3])
    print(1 not in [1,2,3])
    print("y" in "Python")
    print("y" not in "Python")

def FOR(a):
    print(FOR)
    print(a)
    for animal in a:
        print(animal,end=" ")
    else:
        print("정상종료")

def Enumerate(c):
    print(Enumerate)
    #enumerate argment is 2.
    #first count, second List
    for index,color in enumerate(c):
        print(index,color)
    else:
        print("정상종료")

def Break(l):
    print(Break)
    for x in l:
        if x %2 ==0:
            break
        print(x)
    else:
        print("정상종료")

def Continue():
    print(Continue)
    for x in range(10):
        if x%2 == 0 :
            continue
        print(x,end="   ")
    else:
        print("정상종료")

def List_For(a):
    print(List_For)
    #a 리스트 항목 중, 짝수인 것만 2배 하여 result에 저장
    result = [num*2 for num in a if num %2 ==0]
    print(result)
def While_Inside(i):
    print(While_Inside)
    while i<100:
        i+=1
        if i<5:
            continue
        print(i,end="   ")
        if i>10:
            break
    else:
        print("else block")#break 로 for문이 빠져 나가기 때문에 실행되지 않음

def While_TLoop():
    print(While_TLoop)
    while True:
        print("Ctrl +c 를 눌러 루프를 종료하십시오.")

######################################################################################
#main

n=-2;
IF_ELIF_ELSE(n)
money=8500
Conditional_Expression(money)

IN_NOTIN()

animals=['cat','cow','tiger']
FOR(animals)

colors=['red','orange','yellow','green','pink','blue']
Enumerate(colors)

l=[1,3,5,7,9,11,12,13,15,17]
Break(l)
Continue()

a=[1,6,4,13,8,3]
List_For(a)

i=0
While_Inside(i)

While_TLoop()