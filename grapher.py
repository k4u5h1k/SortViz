import matplotlib
matplotlib.use('agg')
import random
import matplotlib.pyplot as plt
from celluloid import Camera

class Plotter():
    def __init__(self, title):
        self.title = title
        self.fig = plt.figure()
        self.camera = Camera(self.fig)

    def plot(self, data, first_highlight, second_highlight=None):
        self.data = data
        self.length = len(data)
        colours = list('b'*self.length)

        colours[first_highlight] = 'r' # First highlight red
        if second_highlight is not None:
            colours[second_highlight] = 'g' # Makes second highlight green (if present)

        plt.bar(list(range(self.length)), data, color=colours)
        plt.title(self.title)
        plt.xlabel("Index")
        plt.ylabel("Magnitude")
        self.camera.snap()

    def animate(self, data, save_file):
        colours = list('g'*len(data))
        plt.bar(list(range(len(data))), data, color=colours)
        plt.title(self.title)
        plt.xlabel("Index")
        plt.ylabel("Magnitude")
        self.camera.snap()
        print(self.camera.animate(repeat=False).to_html5_video(),file=open(f'./templates/{save_file}','w+'))

if __name__=="__main__":
    test = Plotter("Insertion Sort")
    data = list(range(1,15))
    random.shuffle(data) #Just a random list

    for i in range(len(data)):
        temp = data[i]
        j = i-1
        while  j >=0 and temp < data[j]:
            test.plot(data,j+1,j)
            data[j+1] = data[j]
            data[j] = temp
            test.plot(data,j,j+1)
            j -= 1
        data[j+1] = temp

    print(test.animate(data,'1.html'))
