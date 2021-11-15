import math
import matplotlib.pyplot as plt
import numpy as np
class sinus:
    ampl=0
    chast=0
    def __init__(self, a, b):
        self.ampl=a
        self.chast=b
    def vyvod(self):
            t=np.arange(0,1.5,0.01)
            y1=np.sin(math.pi*t*self.chast)*self.ampl
            plt.plot(y1)
            plt.show()

print ('Введите амлитуду и частоту')
amp=2
while amp>1:
    amp=float(input())
    if amp>1 and amp<=0:
        print ('амплитуда синусоиды не может быть больше единицы или меньше нуля!')
        continue
    chas=int(input())
sin=sinus(amp,chas)
sin.vyvod()
