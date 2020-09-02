from grapher import Plotter

class QuickSort():
    def __init__(self,data, filename):
        self.test = Plotter("Quick Sort")
        self.data = data
        self.quickSort(0,len(self.data)-1)
        self.test.animate(self.data,filename)

    def partition(self,low,high): 
        i = (low-1)         # index of smaller element 
        pivot = self.data[high]     # pivot 
      
        for j in range(low , high): 
            if   self.data[j] <= pivot: 
                i = i+1 
                self.test.plot(self.data,j,i)
                self.data[i],self.data[j] = self.data[j],self.data[i] 
                self.test.plot(self.data,i,j)
      
        self.test.plot(self.data,i+1,high)
        self.data[i+1],self.data[high] = self.data[high],self.data[i+1] 
        self.test.plot(self.data,high,i+1)
        return i+1 
      
    def quickSort(self,low,high): 
        if low < high: 
            pi = self.partition(low,high) 
            self.quickSort(low, pi-1) 
            self.quickSort(pi+1, high)
