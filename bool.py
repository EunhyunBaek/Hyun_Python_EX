'''
>,>=,<,<=,==,!= c와 똑같음.

접근방법
직접(direct):int,float,complex,bool
시퀀스(sequence):bytes,str,list,tuple
매핑(mapping):dict

변경가능성
변경 가능(mutable):list,set,dict
변경 불가능(immutable):int,float,complex,bool,bytes,str,tuple

저장모델
리터럴(Literal):int ,float,complex,bool,bytes,str,tuple
저장(container):list,tuple,dict,set

시퀀스 모델: 인덱싱(indexing)과 슬라이싱 (slicing)

+,len(),in,not in (시퀀스 비교 ,길이, 더하기 등 하는방법)
'''
'''
print(12>34) #False 출력
print(True) # True 출력
print(12<34)#True 출력
print(12 != 34)#True 출력
print(type(2))#int
print(type(True))#bool
print(type("Hello Py"))#str
'''
a=['a','b','c','d','e','f']
print(a[2:5])
