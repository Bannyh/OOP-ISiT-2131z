class stak:
    volume=0
    nalito=0
    def __init__(self,a,b):
        self.volume=a
        self.nalito=b
    def otlit(self, x):
            if self.nalito-x<0:
                print('Столько воды в стакане нет')
            else:
                self.nalito-=x
    def dob(self,x):
        if self.nalito+voda>self.volume:
            print('вы перелили, но стакан теперь полон')
            self.nalito = self.volume
        else:
            self.nalito+=x
    def nal(self):
        return(self.nalito)
print('выберите объем стакана')
volume=int(input())
stakan=stak(volume, 0)
while True:
    print('0-разбить 1-налить 2-отлить 3- узнать сколько налито')
    i=int(input())
    if i==0:
        break
    if i==1:
        print('сколько?')
        voda=int(input())
        stakan.dob(voda)
    if i==2:
        print('сколько?')
        voda=int(input())
        stakan.otlit(voda)
    if i==3:
        print(stakan.nal())
