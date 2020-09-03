from grapher import Plotter
import random

class GnomeSort():
    def __init__(self,data,filename):
        self.plotter = Plotter("Gnome Sort")
        self.plotter.animate(self.gnome_sort(data),filename)
    def gnomesort(data): 
        index = 0
        n=len(data)
        while index < n: 
            if index == 0: 
                index = index + 1
            test.plot(data,index,index-1)   
            if data[index] >= data[index - 1]: 
                index = index + 1
            else: 
                data[index], data[index-1] = data[index-1], data[index] 
                self.plotter.plot(data,index-1,index)
                index = index - 1
        return data
