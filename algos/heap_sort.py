from grapher import Plotter

class HeapSort():
    def __init__(self,data,filename):
        self.test = Plotter("Heap Sort")
        self.data = data
        self.heapSort(len(self.data))
        self.test.animate(self.data,filename)

    def heapiy(self, n, i): 
        largest = i 
        l = 2 * i + 1    
        r = 2 * i + 2     

        if l < n and self.data[i] < self.data[l]: 
            largest = l 
  

        if r < n and self.data[largest] < self.data[r]: 
            largest = r 
        if largest != i: 
            self.test.plot(self.data,largest,i)
            self.data[i],self.data[largest] = self.data[largest],self.data[i] 
            self.test.plot(self.data,i,largest)
            self.heapiy(n, largest) 

    def heapSort(self,n): 
 
        for i in range(n//2 - 1, -1, -1): 
            self.heapiy(n, i) 
  
  
        for i in range(n-1, 0, -1): 
            self.test.plot(self.data,0,i)
            self.data[i],self.data[0] = self.data[0],self.data[i] 
            self.test.plot(self.data,i,0)
            self.heapiy(i, 0)

