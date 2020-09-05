from grapher import Plotter

class SelectionSort():
    def __init__(self,data,filename):
        self.test = Plotter("Selection Sort")
        self.test.animate(self.selectionSort(data),filename)

    def selectionSort(self,data):
        for i in range(len(data)): 
            minimum = i 
            for j in range(i+1, len(data)): 
                if data[minimum] > data[j]: 
                    minimum = j         
            self.test.plot(data,minimum,i)
            data[i],data[minimum] = data[minimum],data[i] 
            self.test.plot(data,i,minimum)
        return data
