from algos.insertion_sort import insertion_sort
from algos.bubble_sort import bubble_sort
from algos.quick_sort import QuickSort
from algos.merge_sort import MergeSort

#DOUBLE CHECK THAT THE KEYS ARE SAME IN ALL DICTS

def function_names():
    return {
            'bubble' : bubble_sort,
            'quick' : QuickSort,
            'insertion' : insertion_sort,
            'merge' : MergeSort
            }

def pretty_names():
    return {
            'bubble' :  'Bubble Sort',
            'quick' : 'Quick Sort',
            'insertion' : 'Insertion Sort',
            'merge' : 'Merge Sort'
            }

def filenames():
    return {
            'bubble' : 'bubblesort.html',
            'quick' : 'quicksort.html',
            'insertion' : 'insertionsort.html',
            'merge' : 'mergesort.html'
            }
