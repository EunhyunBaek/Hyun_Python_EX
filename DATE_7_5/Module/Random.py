import random as r

print(ｒ.random())
print(r.randint(1,6))
print(r.randrange(1,100,3))
seqvar=["짬뽕","짜장면","짬짜면"]
r.shuffle(seqvar)
print(seqvar)
print(r.choice(seqvar))