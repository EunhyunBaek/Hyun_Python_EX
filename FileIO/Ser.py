import  pickle
f=open("players.bin","wb")
pickle.dump({"baseball":9},f)
pickle.dump({"soccer":11},f)
pickle.dump({"basketball":22},f)
f.close()

f=open("players.bin","rb")
data_list = []
while True:
    try:
        data_list.append(pickle.load(f))
        print(data_list)
    except EOFError:
        break



f.close()


