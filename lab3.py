class urav:
    netu=False
    cor1=False
    x1=0
    x2=0
    a=0
    b=0
    c=0
    def __init__(self,x,y,z):
        self.a=x
        self.b=y
        self.c=z
    def pereschet(self):
        D=self.b**(2)-4*self.a*self.c
        if D<0:
            self.netu=True
        else:
            self.x1=(self.b*(-1)-D**(0.5))/(2*self.a)
            self.x2=(self.b*(-1)+D**(0.5))/(2*self.a)
            if self.x1==self.x2:
                self.cor1=True
    def vyvod_x(self):
        if not self.netu:
            if not self.cor1:
                return self.x1,self.x2
            else:
                return self.x1
        else:
            return("корней нет!")
    def vyvod_ind(self):
        return a,b,c

while True:
    print('1-задать индексы, 2-вывести корни, 3-вывод индесов, 0-выход')
    i=int(input())
    if i==1:
        print('задайте индексы a,b и с')
        a=int(input())
        b=int(input())
        c=int(input())
        primer=urav(a,b,c)
        primer.pereschet()

    if i==2:
        print(primer.vyvod_x())
    if i==3:
        print (primer.vyvod_ind())
    if i==0:
        break
    
