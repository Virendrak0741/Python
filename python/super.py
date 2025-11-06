#super function
class parent:
    def __init__(self,txt):
        self.txt = txt

    def printmessage(self):
        print(self.txt)

class child(parent):
    def __init__(self,txt):
        super().__init__(txt)

c = child("Hello Virendra")
c.printmessage()