from grapher import Plotter
import random

def insertion_sort(data, filename):
    test = Plotter("Insertion Sort")

    for i in range(len(data)):
        temp = data[i]
        j = i-1
        while  j >=0 and temp < data[j]:
            #I want to show the graph with index j+1 highlighted green and j+1 red
            test.plot(data,j+1,j)

            data[j+1] = data[j]
            data[j] = temp

            #After swapping I want to show the graph with index j highlighted red and j+1 green
            test.plot(data,j,j+1)

            j -= 1

        data[j+1] = temp

    test.animate(data,filename)

def bubble_sort(data, filename):
    test=Plotter("Bubble Sort")

    for i in range(len(data)):
        for j in range(0,len(data)-i-1):
            test.plot(data,j+1,j)
            if data[j+1]<data[j]:
                data[j],data[j+1]=data[j+1],data[j]
                test.plot(data,j,j+1)
    test.animate(data,filename)

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
      
        self.test.plot(self.data,i,high)
        self.data[i+1],self.data[high] = self.data[high],self.data[i+1] 
        self.test.plot(self.data,high,i)
        return i+1 
      
    def quickSort(self,low,high): 
        if low < high: 
            pi = self.partition(low,high) 
            self.quickSort(low, pi-1) 
            self.quickSort(pi+1, high)

if __name__=='__main__':
    bubble_sort("bubble_sort.html")

