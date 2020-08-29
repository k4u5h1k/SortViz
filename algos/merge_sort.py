from grapher import Plotter
import random

class MergeSort():
    def __init__(self,data,filename):
        self.plotter = Plotter("Merge Sort")
        self.plotter.animate(self.merge_sort(data),filename)

    def merge_lists(self,left_sublist,right_sublist):
            i,j = 0,0
            result = []
            while i<len(left_sublist) and j<len(right_sublist):
                    if left_sublist[i] <= right_sublist[j]:
                            result.append(left_sublist[i])
                            i += 1
                    else:
                            result.append(right_sublist[j])
                            j += 1
                    self.plotter.plot(result,len(result)-1)
            result += left_sublist[i:]
            self.plotter.plot(result,len(result)-1)
            result += right_sublist[j:]
            self.plotter.plot(result,len(result)-1)
            return result

    def merge_sort(self,input_list):
            if len(input_list) <= 1:
                    return input_list
            else:
                    midpoint = int(len(input_list)/2)
                    left_sublist = self.merge_sort(input_list[:midpoint])
                    right_sublist = self.merge_sort(input_list[midpoint:])
                    return self.merge_lists(left_sublist,right_sublist)

if __name__=="__main__":
    MergeSort([3,1,2,5,10,2],"merge.html")


