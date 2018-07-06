"""
입출력/로깅(디버긴을 위한)
"""
class P_EX:
    def INFO_FORMAT(self):
        n=input("이름 입력: ")
        j=input("직업 입력: ")
        print('hello,{0}{1}!'.format(n,j))
        print('hello,{1}{0}!'.format(n, j))
        print('hello,{a}{b}'.format(a=n,b=j))
        print('{0}은 {lang}  {1}.'.format(n,j,lang='Python'))
    def OTHER_FORMAT(self):
        print('{0}-{1}-{2}'.format(*'ABC'))                                      #튜플, 리스트형 데이터를 자동으로 언팩킹하여 출력
        print('{0}-{1}-{2}'.format(*['A','B','C']))                              #*는 언팩킹을 한다는 의미
        print('{0[0]}-{0[1]}-{0[2]}'.format(['A','B','C']))                    #리스트형
        print('{0[name]}'.format({'name':'pmk','list_name':'paek'}))          #dict형
        
        print('{:<20}'.format('좌측 정렬') )                                       #정렬
        print('{:>20}'.format('우측 정렬') )
        print('{:^20}'.format('중앙 정렬') )
import math as mt
class MATH:
    def MATH_FORMAT(self):
        print('원주율은 대략 {:f}입니다.'.format(mt.pi))
        print('원주율은 대략 {:.2f}입니다.'.format(mt.pi))

        print('{:+f}; {:+f}'.format(3.14,-3.14))#양수, 음수 기호 반드시 출력
        print('{: f}; {: f}'.format(3.14, -3.14)) #기호는 공백, 음수 기호만 출력
        print('{:-f}; {:-f}'.format(3.14, -3.14)) #기호는 공백, 음수 기호만 출력

        print('{:,}'.format(10000000)) # 천단위 구분자
        print('{:%}'.format(5/12))     # 백분율
        print('{:.2%}'.format(5/12))   # 백분율 자릿수 지정


p=P_EX
m=MATH
#p.INFO_FORMAT(0)
p.OTHER_FORMAT(0)
m.MATH_FORMAT(0)