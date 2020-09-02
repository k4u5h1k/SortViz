from grapher import Plotter
import random

class StoogeSort():
    def __init__(self,data,filename):
        self.test = Plotter("Stooge Sort")
        self.data = data
        self.stoogesort(0,len(self.data)-1)
        self.test.animate(self.data,filename)

    def stoogesort(self,l,h): 

        if l >= h: 
            return
     
        if self.data[l]>self.data[h]: 
            t = self.data[l] 
            self.test.plot(self.data,l,h)
            self.data[l] = self.data[h] 
            self.data[h] = t 
            self.test.plot(self.data,h,l)
       
        if h-l + 1 > 2: 
            t = (int)((h-l + 1)/3) 
       
            self.stoogesort( l, (h-t)) 
       
            self.stoogesort( l + t, (h)) 
       
            self.stoogesort( l, (h-t)) 
