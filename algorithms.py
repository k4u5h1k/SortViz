from algos.insertion_sort import insertion_sort
from algos.bubble_sort import bubble_sort
from algos.quick_sort import QuickSort
from algos.merge_sort import MergeSort
from algos.count_sort import count_sort
from algos.cocktail_sort import CocktailSort
from algos.comb_sort import CombSort
from algos.heap_sort import HeapSort

#DOUBLE CHECK THAT THE KEYS ARE SAME IN ALL DICTS

def function_names():
    return {
            'bubble' : bubble_sort,
            'quick' : QuickSort,
            'insertion' : insertion_sort,
            'merge' : MergeSort,
            'count' : count_sort,
            'cocktail' : CocktailSort,
            'comb' : CombSort,
            'heap' : HeapSort
            }

def pretty_names():
    return {
            'bubble' :  'Bubble Sort',
            'quick' : 'Quick Sort',
            'insertion' : 'Insertion Sort',
            'merge' : 'Merge Sort',
            'count' : 'Count Sort',
            'cocktail' : 'Cocktail Sort',
            'comb' : 'Comb Sort',
            'heap' : 'Heap Sort'
            }

def filenames():
    return {
            'bubble' : 'bubblesort.html',
            'quick' : 'quicksort.html',
            'insertion' : 'insertionsort.html',
            'merge' : 'mergesort.html',
            'count' : 'countsort.html',
            'cocktail' : 'cocktailsort.html',
            'comb' : 'combsort.html',
            'heap' : 'heapsort.html'
            }
