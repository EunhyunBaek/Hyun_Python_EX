"""
id,pass 입력 받아서 로그인 수행
    -id는 이메일로
    -비밀번호 길이 6~12자 사이여야 한다. <- len 활용
    -id, 비밀번호 영문자, 숫자 포함해야 함
    -id, 비밀번호 영문 대문자 허용하지 않음.

isalpha 문자열 알파벳 구성 여부 확인하기.
https://dongyeopblog.wordpress.com/2016/06/27/python-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%95%8C%ED%8C%8C%EB%B2%B3%EA%B5%AC%EC%84%B1-%EC%97%AC%EB%B6%80%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0-isalpha/

문자열 패턴
http://neoryuee.tistory.com/69
"""
import  re
def CheckPassWorld(passwold):
    count=0
    patten=["[1-9]","[a-z]","[A-Z]"]
    for a in patten:
        m1=re.findall(a,passwold)
        print(m1)
        print(a)
        if m1==[]:
            if a!="[A-Z]":
                count+=1
    return count

class Information:
    IN_ID=str();
    IN_PASS=str();

    def SET_PASS(passwold):
        if 6<=len(passwold)<=12:
            a=CheckPassWorld(passwold)
            if a==0:
                IN_PASS=passwold
                print("가입성공")
            else:
                print("가입 실패")
        else:
            print("pass 실패")

    def SET_ID(ID):
        result_list = re.findall(r"(\w+[\w\.]*)@(\w+[\w\.]*)\.([A-Za-z]+)", ID)
        if result_list == []:
            print("id 실패")
        else:
            print("성공")
            IN_ID=ID;
            Information.SET_PASS(input("pass를 입력해 주세요:"))

    def GET_ID(self):
        pass
    def GET_PASS(self):
        pass


Information.SET_ID(input("id를 입력해 주세요:"))

