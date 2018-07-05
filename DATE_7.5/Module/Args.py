import  sys
args = sys.argv[1:]#arg[0]는 스크립트명 자체

for x in args:
    print(x,end=" ")
else:
    print()
"""
(venv) D:\hyun_py\Hyun_Python_EX\DATE_7.5\Module>python Args.py hello
hello
"""