def fib(n):                 # n까지의 피보나치 수열을 출력하는 함수
    a,b=0,1
    while b<n:
        print(b,end=' ')    # end 기본 값인 줄 넘기기 대신 공백으로 한 줄에 출력
        a,b,=b,a+b
        print()              # 줄넘기기

def fib2(n):                 # n 까지의 피보나치 수열을 반환 하는 함수
    result = []               # 피보나치 수 저장을 위한 리스트 초기화
    a,b = 0,1
    while b<n:
        result.append(b)      # 리스트 값 채우기
        a,b=b,a+b
    return result            #  피보나치 수 리스트 반환
################################################################################
if __name__=="__main__":    # 외부에서 호출 시
    import sys
    print("메인콜")
    try:
        fib(int(sys.argv[1]))
    except IndexError:
        print("인덱싱 할 수 없습니다.")
else:
    print()
################################################################################
for key in sys.modules.keys():
    print(key)

"""
파이참 하단 Terminal 활용

(venv) D:\hyun_py>cd Hyun_Python_EX

(venv) D:\hyun_py\Hyun_Python_EX>cd DATE_7_5

(venv) D:\hyun_py\Hyun_Python_EX\DATE_7_5>cd Module

(venv) D:\hyun_py\Hyun_Python_EX\DATE_7_5\Module>python Fibo.py 50
메인콜
1
1
2
3
5
8
13
21
34


"""