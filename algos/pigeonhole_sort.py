from grapher import Plotter

class PigeonholeSort():
    def __init__(self,data,filename):
        self.plotter = Plotter("Pigeonhole Sort")
        self.plotter.animate(self.pigeonholesort(data),filename)

    def pigeonholesort(self,data): 
        my_min = min(data) 
        my_max = max(data) 
        size = my_max - my_min + 1 
        holes = [0] * size 
        self.plotter.plot(data,len(data)-1)
       
        for x in data: 
            holes[x - my_min] += 1 
        i = 0
        for count in range(size): 
            while holes[count] > 0: 
                holes[count] -= 1
                data[i] = count + my_min 
                self.plotter.plot(data,len(data)-1,i)
                i += 1
        return data

if __name__ == "__main__":
    import random
    data = list(range(1,11))
    random.shuffle(data)
    Pigeonhole_Sort(data,"pigeonholesort.html")
