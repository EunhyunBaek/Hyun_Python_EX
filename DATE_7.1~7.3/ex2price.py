#global은 키워드이다. 변수명으로 사용 할 수 없다.
#키워드 목록 확인하는 방법 keyword.kwlist

import keyword as key
price,vat= 120000 , 0.1
vat2 = vat3 =vat
final_price = price +(price * vat3)
e,f = 3.5,5.3
e,f=f,e
print(final_price)
print(e,f)
value=100
_value=200
value3=300
print(key.kwlist)