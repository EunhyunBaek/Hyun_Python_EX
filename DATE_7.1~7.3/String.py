######################################################################################
'''
str = string 형태이다.
문자열 메서드     대소문자 관련
upper()         문자열을 대문자로 변환
lower()         문자열을 소문자로 변환
swapcase()      대 <-> 소문자를 전환
capitalize()    문자열의 첫 글자를 대문자로 변환
title()         문자열의 각 단어의 첫글자를 대문자로 변환

문자열 메서드     검색 관련
count()         문자열 내 검색어 개수를 반환
find()          문자열 내 첫번째 검색된 위치의 인덱스를 반환
index()         문자열 내 검색된 위치의 인덱스를 반환
rindex()        문자열 내 오른쪽으로부터 검색된 위치의 인덱스를 반환
startswith()    문자열이 지정된 검색어로 시작하는지 여부 반환
endswith()      문자열이 지정된 검색어로 끝나는지 여부 반환

문자열메서드      편집 치환 관련
strip()         문자열 내 좌우 공백문자를 삭제, 좌우 삭제할 문자열을 지정 가능
lstrip()        문자열 내 왼쪽의 공백문자를 제거
rstrip()        문자열 내 오른쪽 공백문자를 제거
replace()       문자열 내 지정된 검색어를 다른 문자열로 치환

문자열 메서드     정렬 관련
center()        문자열을 가운데로 정렬
ljust()         문자열을 왼쪽으로 정렬
rjust()         문자열을 오른쪽으로 정렬
zfill()         자리수를 지정하고 빈 공간을 0로 채움

문자열 메서드      분리, 결합 관련
split()         문자열을 공백문자(혹은 지정된 문자)를 기준으로 분리
rsplit()        문자열을 공백문자(혹은 지정된 문자)를 기준으로 오른쪽부터 분리
join()          문자열을 지정된 기호로 합침
splitlines()    문자열을 개행문자를 기준으로 분리

문자열 메서드     판별 관련
isdigit()       문자열이 숫자로 구성되어 있는가 여부를 반환
isalpha()       문자열이 알파벳으로 구성되어 있는가 여부를 반환
islower()       문자열이 소문자로 구성되어 있는가 여부를 반환
isupper()       문자열이 대문자로 구성되어 있는가 여부를 반환
isspace()       문자열이 공백문자로 구성되어 있는가 여부를 반환

문자열 메서드     서식 메서드 - 문자열 포맷 코드
%s              문자열(string)%c              문자 1개(character)
%d              정수(integer)
%f              부동 소수(floating point)
%o              8진수
%x              16진수
%%              Literal %
'''
######################################################################################
#function
def Type(a):
    print(type(a))
def Isinstance(a,b):
    print(isinstance(a,b))
def H_print(a):
    print(a)

def H_PlusStr(a,b,c):
    whilevalue=0
    while(whilevalue>c):
        print("your first   name   :   %s"%a)
        print("your last    name   :   %s"%b)
        print("your full    name   :   %s"%(a+b))
        whilevalue=whilevalue+1

def H_SlicingIndex(a):
    print(len(a))
    print(a[2])
    print(a[8:11])
    print(a[-7:-1])
    print(a[5:])
    print(a[len(a)-1])
    print(a[:-1])

def H_LOWER_UPPER_STRING(a):
    print(a.upper())
    print(a.lower())
    print(a.swapcase())
    print(a.capitalize())
    print(a.title())
def H_SURCH(a):
    print("surch")
    print(a.find('Like'))
    print(a.find('Like',5))
    print(a.find('JS'))
    print(a.rfind('Like'))
    print(a.rindex('Like'))
    print(a.startswith('I Like'))
    print(a.startswith('Like',2))
    print(a.endswith('Also'))
    print(a.endswith('Java',0,26))
def H_EDIT(a):
    print('edit')
    print(a.strip())
    print(a.rstrip())
    print(a.lstrip())
    a='<><abc><><defg><><>'
    print(a.strip('<>'))
    a='Hello Java'
    print(a.replace('Java','Python'))

def H_ALIEN(a):
    print("ALIEN")
    print(a.center(60))
    print(a.center(60,'-'))
    print(a.ljust(60, '-'))
    print(a.rjust(60, '-'))
    print('20'.zfill(5))
    print('1234'.zfill(5))

def H_SPLIT(a):
    print("SPLIT")
    t=a.split()
    print(t)
    t=a.split(' and ')
    print(t)
    a2=":".join(t)
    print(a2)
    a3="one:two:three:four:five"
    print(a3.split(':',2))
    print(a3.rsplit(':',2))

    lines = '''1st line
2nd line
2rd line
4th line
'''
    print(lines.splitlines())
def H_Discrimination():
    print(H_Discrimination)
    print('1234'.isdigit())
    print('abcd'.isalpha())
    print('1234'.isalpha())
    print('asdf'.isdigit())
    print('abcd'.islower())
    print('ABCD'.isupper())
    print('\n\n'.isspace())
    print(' '.isspace())
    print(''.isspace())
def H_String_Format(a,b):
    print(H_String_Format)
    print("i have {} apples, and I ate {} apples.".format(a,b))
    print("i have {total} apples, and I ate {num} apples.".format(total=a,num=b))
    print("i have {total} apples, and I ate {num} apples.".format_map({"total":a, "num":b}))
    print("interest rate is %f" %1.24)
    print("interest rate is %2.4f" % 1.24)
######################################################################################
#main
s="Life is too short, You need Python!"
str1 = "hello world"
str2 = "life is too short, you need python"
Type(str),Type(str1),Type(str2)
Isinstance(str1,str)

str3 ="""
...abcdefg
...가나다라마바사
...123456789
...이것은 str3입니다."""

H_print(str3)

first_name = "hyun"
last_name = "Beak"
H_PlusStr(first_name,last_name,5)
H_SlicingIndex(s)

s= "I Like Python. I Like Java Also"
H_LOWER_UPPER_STRING(s)
H_SURCH(s)

s= ' spam and ham '
H_EDIT(s)

s='Alice and the Heart Queen'
H_ALIEN(s)

s= ' spam and ham '
H_SPLIT(s)

H_Discrimination()

a,b=5,3
H_String_Format(a,b)
######################################################################################