'''
파이썬 자료구조? :list,set,map

add(x)          세트에 x를 추가
remove(x)       세트에서 x를 제거. x가 세트에 없으면 오류 발생
discard(x)      세트에서 x를 제거. x가 세트에 없으면 무시
update({set})   세트에 여러 개의 값을 추가
clear()         세트를 비움

세트(set)란
    순서가 없고 중복이 없는 객체들의 집합 (non sequence).{}기호로 정의
        len(),in,not in 정도만 가능
    수정이 가능한(mutable) 자료형
    수학의 집합을 표현할 때 사용한다.
세트(Set)는 교집합,합집합,차집합을 구하는데 유용하게 사용
교집합(set)            a&b         a.intersection(b)
합집합(set)            a|b         a.union(b)
차집합(set)            a-b         a.difference(b)
모집합(bool)                       a.issuperset(b)
부분집합(bool)                     a.issubeset(b)
'''
############################################################################
#function
def List_method(a):
    print(List_method)
    a.append(5)
    print(a)
    a.insert(3,4)
    print(a)
    print(a.count(2))
    a.reverse()
    print(a)
    a.sort()
    print(a)
    a.remove(3)
    print(a)
    a.extend([6,7,8])
    print(a)
def List_Queue(a):
    print(List_Queue)
    queue.append(100)
    queue.append(200)
    queue.append(300)
    print(queue)

    #print(queue.append(400)) #None 출력
    print(queue.pop(0))#가장 앞쪽의 인덱스 pop FIFO
    print(queue.pop(0))
    print(queue)

def List_Stack(a):
    print(List_Stack)
    stack.append(10)
    stack.append(20)
    stack.append(30)

    print(stack)

    print(stack.pop())#가장 뒤쪽의 인덱스 pop LIFO
    print(stack.pop())
    print(stack)

def Sort(a):
    print(Sort)
    a.sort(key=str)
    print(a)
    a.sort(key=int)
    print(a)
    a.sort()
    print(a)
    a.sort(reverse=True)
    print(a)

def Set(a):
    print(Set)
    print(a,type(a))
    print(len(a))
    print(2 in a)
    print(2 not in a)

def Set2(a,b):
    print(Set2)
    print("a       =       %s"%a)
    print("b       =       %s"%b)
    c=a.union(b)#합집합
    print("합집합          %s"%c)
    d=a.intersection(b)#교집합
    print("교집합:         %s"%d)
    d=a.difference(b)#차집합
    print("차집합:         %s"%d)
    e=a.symmetric_difference(b)
    print("대칭 차이?:     %s"%e)

    print("a,d모집합:      %s"%a.issuperset(d))
    print("e,a모집합:      %s"%e.issuperset(a))
    print("b,c부분집합:    %s"%b.issubset(c))


############################################################################
#main
a=[1,2,3]
List_method(a)
queue = []
List_Queue(queue)
stack=[]
List_Stack(stack)
a=[1,2,22,10,9,8,33,4,11]
Sort(a)
a={1,2,3}
Set(a)
s1={1,2,3,4,5,6,7,8,9,10}
s2={10,20,30}
Set2(s1,s2)