'''
사전(dict)
    순서를 가지지 않는 객체의 집합
    Key 기반으로 값을 저장하고 참조하는 매핑형 자료형
    시퀀스 자료형이 아니므로 len(), in ,not in 정도만 가능

    사전의 메소드
        메서드                          설명
        keys()                          사전내 키 목록을 dict_keys 객체로 반환
        values()                        사전내 값 목록을 dict_values 객체로 반환
        items()                         사전내 키-값 쌍을 튜플로 묶은 dict_items 객체로 반환
        get(key{,default})              사전내 key에 대응하는 값을 반환
                                        default를 지정하면 key에 대응하는 값이 없을 때 default를 반환
        del dic[key]                    dic 사전 내 key에 대응하는 객체를 삭제
        clear()                         사전을 비움

    dict_keys,  dict_values,    dict_items를 리스트로 사용하려면 list() 함수를 활용

    사전의 키(key)
        사전의 키는 해싱해야 하기 때문에 수정 불가능한 객체여야 한다.
            예)bool,수치형(int, float,  complex),   str,    tuple
'''

######################################################################################
#function
def Dict(d):
    print(Dict)
    print(d)
    print(d['basketball'])

    d['volleyball']=6
    print(d)

    print(len(d))
    print('soccer'in d)
    print('volleyball' not in d)
def Print_Dict():
    print(Print_Dict)
    d = dict()  # empyty dict
    print(d)
    d = dict(one=1, two=2)  # keyword arguments
    print(d)
    d = dict([('one', 1), ('two', 2)])  # tuple list
    print(d)
    keys = ('one', 'two', 'three')
    values = (1, 2, 3)
    d = dict(zip(keys, values))
    print(d)
def Dict_Key(d):
    print(Dict_Key)
    print(d)

    d[True]='true'
    d[10]='10'
    d["twenty"]='20'
    d[(1,2,3)]='6'

    print(d)

    #d[[1,2,3]]='6' #TypeError 발생
def Dict_Method(d):
    print(Dict_Method)
    d['volleyball'] = 6

    print(d.keys())#key 목록 가져오기
    print(d.values())#value 목록 가져오기
    print(d.items())#튜플 목록 가져오기

    #x=d['bandball']#KeyError
    x=d.get('handball')
    print(x)

    del d['soccer']
    print(d)

    d.clear()
    print(d)

def Dict_Circuit(d):
    print(Dict_Circuit)

    for key in d:
        print(str(key)+"      :       "+str(d[key]),end='    ')
    else:
        print()

    for key in d.keys():
        print("{0}      :       {1}".format(key,d[key]),end='    ')
    else:
        print()
    for key,value in d.items():
        print("{0}      :       {1}".format(key,d[key]),end='    ')
    else:
        print()

    for key,value   in d.items():
        print("{0}      :       {1}".format(key,value),end='    ')
    else:
        print()

######################################################################################
#main
d={'basketball':5,'soccer':11,'baseball':9}

Dict(d)

Print_Dict()

d={}
Dict_Key(d)

d={'basketball':5,'soccer':11,'baseball':9}
Dict_Method(d)

d={'basketball':5,'soccer':11,'baseball':9}
Dict_Circuit(d)