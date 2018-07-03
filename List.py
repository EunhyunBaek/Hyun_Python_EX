'''
180703
리스트:리스트의 메서드
    append(x)       리스트의 마지막에 x를 추가
    insert(i,x)     리스트 인덱스 i 위치에 x를 추가
    reverse()       리스트를 역순으로 뒤집은
    sort()          리스트 요소를 순서대로 정렬
    remove(i)       리스트 인덱스 i에 있는 요소를 제거
    extend(l)       리스트 마지막에 리스트 l을 추가
    index(x)        인덱스 내에 x가 있으면 인덱스값을 반환 없으면 -1
    count(x)        리스트 내에 x가 몇 개 있는지 그 개수를 반환

리스트란?
    순서를 가지는 객체들의 집합, 파이썬 자료형들중 가장 많이 사용

리스트 생성과 연산
    시쿼스 자료형: 시퀀스 연산(인덱싱,슬라이싱,연결,반복,len,in,not in) 가능
    변경 가능(mutable) 자료형이므로 항목의 추가, 변경, 삭제 모두 가능
'''
############################################################################
#function
def Slice_List(l):
    print(Slice_List)
    print(l[-2])
    print(l[-1])
    print(l[1:3])
    print(1 * 2)
    print(l * 2)
    print(l + [3, 4, 5])
def Slice_List2(a):
    print(Slice_List2)
    a[2]=a[2]+90
    print(a)
def Slice_List3(a):
    print(Slice_List3)
    #슬라이스를 이용한 치환의 예
    a[0:2]=[10,20]
    print(a)
    a[0:2] =[10]
    print(a)
    a[0:2] =[20]
    print(a)
    a[0:2] =[30]
    print(a)
def List4(a):
    print(List4)
    print(a[-2],a[-1],a[0],a[1],a[2])
    print(a[1:3])
    print(a*2)
    print(a+[3,4,5])
    print(len(a))
    print(2 in a)
    del a[0]
    print(a)
def Slice_del(a):
    print(Slice_del)
    a[1:2]=[]
    print(a)
    a[0:]=[]
    print(a)
def Slice_insert(a):
    print(Slice_insert)
    a[1:1]=['a']
    print(a)
    a[5:]=[12345]
    print(a)
    a[:0]=[-12,-1,0]
    print(a)
############################################################################
#main
l = [1, 2, 'Python']
Slice_List(l)
a=['apple','banana',10,20]
Slice_List2(a)
a=[1,12,123,1234]
Slice_List3(a)
a=[1,12,123,1234]
Slice_del(a)
Slice_insert(a)

List4(l)
l = [1, 2, 'Python']
List4(l)

############################################################################