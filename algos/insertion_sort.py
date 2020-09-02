from grapher import Plotter

class InsertionSort():
    def __init__(self,data,filename):
       self.plotter = Plotter("Insertion Sort") 
       self.insertion_sort(data)
       self.plotter.animate(self.insertion_sort(data),filename)

    def insertion_sort(self,data):
        for i in range(len(data)):
            temp = data[i]
            j = i-1
            while  j >=0 and temp < data[j]:
                #I want to show the graph with index j+1 highlighted green and j+1 red
                self.plotter.plot(data,j+1,j)

                data[j+1] = data[j]
                data[j] = temp

                #After swapping I want to show the graph with index j highlighted red and j+1 green
                self.plotter.plot(data,j,j+1)

                j -= 1

            data[j+1] = temp

        return data

