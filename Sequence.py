############################################################################
'''
180702
수치형
숫자를 다루는 데이터형
수치형 데이터끼리는 더하기, 빼기 드으이 산술연산을 할 수 있다
수치형의 종류
정수:int
실수형,부동소수점(소수): float
복소수:complex
파이썬 3버전에서는 long형이 없어지고 모두 int 형으로 처리된다.

수치형 :내장 수치 함수
abs 절대값
int 정수변환
float 실수변환
complex 허수 생성
divmod 나눗셈 몫과 나머지
pow 제곱

a<<b a의 비트를 b번 왼쪽으로 이동
a>>b a의 비트를 b번 오른쪽으로 이동
a&b a와 b의 비트를 and연산
a와 b의 비트를 or연산
a^b a와 b의 비트를 xor연산
~x x의 비트를 뒤집음

############################################################################
180703

############################################################################
'''
############################################################################
#function
def pr(a,b):
    if(a>b):
        print("%d가 크다"%a)
        print(True)
    else:
        print("%d가 작다"%b)
        print(False)

def isinst(a,int):
    print("%d는 %s입니다."%(a,type(a)))
    print("결과는 %s 입니다."%isinstance(a,int))
def is_int(a):
    print("a는 정수가 %s"%a.is_integer())
def LotationNumber(a) :
    print("10진수 %s"%a)
    print("2진수 %s"%bin(a))
    print("8진수 %s"%oct(a))
    print("16진수 %s"%hex(a))

def Type(a):
    print("%s 의 형태는 %s"%(a,type(a)))
    if(type(a)==complex):
        print("실수부:%s 허수부 %s"%(a.real,a.imag))
def IntC(a):
    print("정수형태:%s"%int(a))
def BitCalculate(a,b,c):
    if(c==0):
        print(bin(a<<b))
    elif(c==1):
        print(bin(a>>b))
    elif(c==2):
        print(bin(a&b))
    elif (c == 3):
        print(bin(a|b))
############################################################################
#180703
#순차 자료형(Sequence) 내장 함수:range
'''
range({start=0,}end{,step=1})
start부터 end까지의 순차적 리스트를 step 간격으로 생성
'''
def Sequence_Range():
    print(Sequence_Range())
############################################################################
############################################################################



############################################################################
#main
a,b=10.5,3
#complex 함수를 활용해 복소수타입 생성 가능
#cpx=4+5j
cpx=complex(7,-2)#complex(실수,허수부)
pr(a,b)
isinst(a,int)
isinst(a,float)
is_int(a)
LotationNumber(b)
Type(cpx)
IntC(a)
a,b,c=16,2,0
BitCalculate(a,b,c)

############################################################################