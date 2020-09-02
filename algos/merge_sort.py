from grapher import Plotter

class MergeSort():
    def __init__(self,data,filename):
        self.plotter = Plotter("Merge Sort")
        self.length = len(data)
        self.plotter.plot(data,0)
        self.plotter.plot(data,0)
        self.plotter.animate(self.merge_sort(data,0),filename)

    def merge_lists(self,left_sublist,right_sublist,start):
            i,j = 0,0
            result = []
            while i<len(left_sublist) and j<len(right_sublist):
                    if left_sublist[i] <= right_sublist[j]:
                            result.append(left_sublist[i])
                            i += 1
                    else:
                            result.append(right_sublist[j])
                            j += 1
                    self.plotter.plot([0]*start+result+[0]*(self.length-start-len(result)),start+len(result)-1)
            result += left_sublist[i:]
            self.plotter.plot([0]*start+result+[0]*(self.length-start-len(result)),start+len(result)-1)
            result += right_sublist[j:]
            self.plotter.plot([0]*start+result+[0]*(self.length-start-len(result)),start+len(result)-1)
            return result

    def merge_sort(self,input_list,start):
            if len(input_list) <= 1:
                    return input_list
            else:
                    midpoint = int(len(input_list)/2)
                    left_sublist = self.merge_sort(input_list[:midpoint],start)
                    right_sublist = self.merge_sort(input_list[midpoint:],start+midpoint)
                    return self.merge_lists(left_sublist,right_sublist,start)
