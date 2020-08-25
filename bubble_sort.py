from grapher import Plotter
import random 

def bubble_sort(filename):
    test=Plotter("Bubble Sort")
    data = list(range(1,15))
    random.shuffle(data)
    for i in range(len(data)):
        for j in range(0,len(data)-i-1):
            test.plot(data,j+1,j)
            if data[j+1]<data[j]:
                data[j],data[j+1]=data[j+1],data[j]
                test.plot(data,j,j+1)
    test.animate(data,filename)

bubble_sort("bubble.html")
