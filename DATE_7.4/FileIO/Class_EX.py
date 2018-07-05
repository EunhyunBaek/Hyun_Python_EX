class CVS:
    def __init__(self,name):
        self.name=name
    def Name(self):
        print("안녕하세요 SevenStore " + self.name, "지점 입니다.")
    def Buy(self):
       pass

class SevenStore(CVS):
    pass
class MiniShop(CVS):
    pass
class CvsyoU(CVS):
    pass
class GS25(CVS):
    pass

Store=SevenStore("광명")
Store.Name()