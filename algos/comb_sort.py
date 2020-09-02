from grapher import Plotter

class CombSort():
    def __init__(self,data,filename):
        self.test = Plotter("Comb Sort")
        self.data = data
        self.combSort(len(self.data))
        self.test.animate(self.data,filename)

    def getNextGap(self,gap): 
        gap = (gap * 10)//13
        if gap < 1: 
            return 1
        return gap 

    def combSort(self,n): 
        gap = n 
  
        swapped = True
        while gap !=1 or swapped == 1: 
  
       
            gap = self.getNextGap(gap)
            swapped = False
            for i in range(0, n-gap): 
                if self.data[i] > self.data[i + gap]: 
                    self.test.plot(self.data,i,i+gap)
                    self.data[i],self.data[i+gap] = self.data[i+gap],self.data[i] 
                    self.test.plot(self.data,i,i+gap) 
                    swapped = True
    
    
