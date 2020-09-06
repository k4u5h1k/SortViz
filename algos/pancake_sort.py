from grapher import Plotter

class PancakeSort():
    def __init__(self,data,filename):
        self.plotter = Plotter("Pancake Sort")
        self.plotter.animate(self.pancakesort(data),filename)

    def flip(self,arr, i): 
        start = 0
        while start < i: 
            
            self.plotter.plot(arr,i,start)
            arr[start],arr[i] = arr[i],arr[start] 
            self.plotter.plot(arr,start,i)
            start += 1
            i -= 1

    def findMax(self,arr, n): 
        mi = 0
        for i in range(0,n): 
            if arr[i] > arr[mi]: 
                mi = i 
        return mi 
  

    def pancakesort(self, data):
        curr_size = len(data)
        while curr_size > 1: 
            mi = self.findMax(data, curr_size) 
            if mi != curr_size-1:  
                self.flip(data, mi) 
                self.flip(data, curr_size-1) 
            curr_size -= 1
  
        return data

if __name__ == "__main__":
    import random
    data = list(range(1,11))
    random.shuffle(data)
    PancakeSort(data,"pancakesort.html")

