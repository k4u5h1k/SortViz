from grapher import Plotter

class CountSort():
    def __init__(self,data,filename):
        self.plotter = Plotter("Count Sort")
        self.plotter.animate(self.count_sort(data),filename)

    def count_sort(self,data):
        array = [0]*(max(data)+1)
        result = []
        self.plotter.plot(data,len(data)-1)
        for element in data:
            array[element] += 1

        for index, element in enumerate(array):
            if element != 0:
                result.append(index)
                self.plotter.plot(result,len(result)-1)

        return result
