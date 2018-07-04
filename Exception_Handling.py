'''
예외 처리
오류는 프로그램이 잘못 작동되는 것을 막기 위한 파이썬의 처리
이 오류를 회피하기 위한 동작을 예외 처리라 한다

list =[]
list[0] # 내부에 0인덱스에 매칭되는 값이 없으므로 IndexError를 발생

text="Try convert me to int"
number = int(text)#정수 형식의 문자열이 아니여서 변환이 불가 :ValueError

result = 4/0 # 0으로는 나눗셈을 할 수 없다. ZeroDivisonError 발생

'''
#####################################################################
#function
#특정 오류의 회피- try,except
def TRY_EXCEPT():
    try:
        4/0
    except ZeroDivisionError as e:
        print("오류발생%s"%e)
#예외처리 -try, except, else
def TRY_EXCEPT_ELSE():
    try:
        f=open("notexists.txt","r")
    except FileNotFoundError as e:
        print(e)
    else:
        data=f.read()
        f.close()
#예외 처리 - try ~ finally
def TRY_FINALLY():
    f=open("result.txt","r")
def List_args():
    list(range(3,6))
    args=[3,6]
    list(range(*args))
def intro_mycar(manu,seats=4,type="sedan"):
    print("내차는",manu,'의',seats,'인승',type,'이다')

#####################################################################
#main


TRY_EXCEPT()
TRY_EXCEPT_ELSE()
input={'manu':'현대','seats':9,'type':'승합차'}
intro_mycar(**input)