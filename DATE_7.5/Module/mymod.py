Pi=3.13159

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

################################################################################
def main():
    print("mymod.py를 최상위 모듈로 싱행했습니다.")
if __name__=="__main__":
    main()
else:
    print("mymod.py의 모듈 이름: "+__name__)