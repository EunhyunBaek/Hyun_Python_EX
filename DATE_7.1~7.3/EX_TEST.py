from Hyun_Python_EX.EX_TEST2 import BOOKSTORE


def GGD(i):
    print(GGD)
    if(i!=10):
        for (x) in range(1,10):
            data=x*i
            print(data)
    else:
        for x in range(1,10):
            for y in range(1,10):
                print(x*y)


def Change_String(a):
    print(Change_String)
    print("UPPER:%s"%a.upper())
    print("LOWER:%s" % a.lower())
    print("SWAP:%s"%a.swapcase())
def Reverse(c):
    c =c[::-1]
    print(c)

def Dict_Method():
    print(Dict_Method)

    BookList = []
    BookName=['python','Machine Learing','java','Deep Learning','IOT']
    WriteComp=["비트","한국","비트","한국","한국"]
    BookPage=[510,380,400,600,550]
    Recommendation=["T","T","F","T","T"]

    Size=len(Recommendation)

    for x in range(Size):
        comcent=[WriteComp[x],BookPage[x],Recommendation[x]]
        BookList.append(comcent)

    for x in range(Size):
        print(BookName[x].rjust(20),BookList[x])

#page 500이상
    print("page 500")
    for x in range(Size):
        if(BookList[x][1]>500):
            print(BookName[x].rjust(20), BookList[x])
#추천목록 T
    print("추천목록")
    for x in range(Size):
        if(BookList[x][2]=="T"):
            print(BookName[x].rjust(20), BookList[x])
#페이지 합계
    sum=0
    for x in range(5):
        sum=sum+int(BookList[x][1])
    print("읽은 페이지수 합계:  "+str(sum))
#출판사 목록
    print("출판사 목록")
    pub = set()
    for x in range(Size):
        pub.add(BookList[x][0])
    print(pub)
#출판사별 출력
    for a in pub:
        print(a)
        for x in range(Size):
            if (BookList[x][0] == a):
                print(BookName[x].rjust(20), BookList[x])


###########################################################################
#main
i=1
GGD(i)
a=int(input("구구단 단수 입력:"))
GGD(a)

b=input("Lower,Upper,SWAP:   ")
Change_String(b)

c=input("Reverse:   ")
Reverse(c)


#Dict_Method()
BOOKSTORE()