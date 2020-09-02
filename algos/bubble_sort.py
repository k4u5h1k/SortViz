from grapher import Plotter

class BubbleSort():
    def __init__(self,data,filename):
        self.plotter = Plotter("Bubble Sort")
        self.plotter.animate(self.bubble_sort(data),filename)

    def bubble_sort(self,data):
        for i in range(len(data)):
            for j in range(0,len(data)-i-1):
                self.plotter.plot(data,j+1,j)
                if data[j+1]<data[j]:
                    data[j],data[j+1]=data[j+1],data[j]
                    self.plotter.plot(data,j,j+1)
        return data


