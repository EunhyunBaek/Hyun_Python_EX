'''
파일 입출력 개요:파일의 생성과 파일 모드
    파일객체 = open({파일명},{파일모드}[,encoding='인코딩'])
함수명          설명
open            파일을 생성한다
write           파일에 내용을 기록한다
read            파일에서 내용을 읽어온다
close           파일 사용을 끝낸다.
                파일을 열었으면(open) 반드시 사용후 닫아주도록 한다.
seek            사용자가 원하는 위치로 파일 포인터 이동
tell            현재 파일에서 어디까지 읽고 썻는지 위치를 반환
파일 입출력 개요:readline 함수를 이용한 텍스트 파일 읽기

파일 입출력 개요:with ~ as = 자동 자원 정리
    with ~ as 를 이용,파일 입출력을 수행하면 수동으로 파일을 close 하지 않아도 된다.

Using Pickle
    객체의 내용을 파일에 저장하거나 복원해야 할 경우에 Pickle 모듈을 사용하면 편리
    Pickle 모듈은 객체를 파일에 썻다가 나중에 복원할 수 있도록 객체를 바이트 스트림으로 직렬화
        모든 파이썬의 객체를 저장하고 읽을 수 있음
        원하는 객체를 형태 변환 없이 쉽게 쓰고 읽을 수 있다
    Pickle 모듈을 사용하려면 import pickle 을 이용, 모듈을 로드해야 한다
    Pickle 모듈 주요 메서드
        메서드                             설명
        dump(data,file[,protocol])          data 객체를 [protocol을 이용해] file에 저장
        load(file)                          File로부터 저장된 객체를 불러옴
'''

def File_Write_Sample():
    f= open('text.txt','w',encoding='utf-8')
    write_size=f.write("Life is too short, You need Python")
    print(write_size)
    f.close()
def File_Read_Sample():
    f= open('text.txt','r',encoding='utf-8')
    text=f.read()
    print(text)
    f.close()

def Readline():
    f=open('multilines.txt','w',encoding='utf-8')
    for i in range(1,10):
        f.write("%d:Life is too short, You need Python \n"%i)
    f.close()
    print("read")
    f=open('multilines.txt','r',encoding='utf-8')
    text=f.read()
    print(text)
    f.close()
    print("readline")
    f = open('multilines.txt', 'r', encoding='utf-8')
    while True:
        line=f.readline()
        if not line:
            break
        print(line)
    f.close()

#main
File_Write_Sample()
File_Read_Sample()
Readline()