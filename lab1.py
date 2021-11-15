class dver:
    close=False
    close_k=False
    key=0
    def __init__(self,x,y,z):
        self.close=x
        self.close_k=y
        self.key=z
    def zaper(self):
        self.close_k=True
        self.close=True
    def otkr(self):
        self.close=False
        self.close_k=False
    def new_key(self, nkey):
        self.key=nkey
    def close_d(self):
        self.close=True
door=dver(False,False,0)
while True:
    if door.close_k and door.close:
        print('Дверь заперта на ключ 1-открыть, 0-уйти ')
        i=int(input())
        if i==0:
            break
        if i==1:
            while True:
                print('введите ключ')
                key=int(input())
                if key==door.key:

                    print('Дверь отперта')
                    door.otkr()
                    break
                if key!=door.key:
                    print('пароль неверный попробуйте еще раз')
    if not door.close_k and not door.close:
        print ('дверь открыта, 1- закрыть, 0- уйти')
        i= int(input())
        if i==0:
            break
        if i==1:
            door.close_d()
            
    if door.close and not door.close_k:
        print('дверь закрыта 1-запереть, 0-открыть')
        i=int(input())
        if i==1:
            print('запереть с новым ключом или использовать старый 0-старый 1 -новый')
            j=int(input())
            if j==0:
                door.zaper()
            if j==1:
                print('Новый ключ')
                key=int(input())
                door.new_key(key)
                door.zaper()
        if i==0:
            door.otkr()
                      

        
                
                
