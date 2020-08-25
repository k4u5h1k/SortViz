#!/usr/bin/env python3
from flask import Flask
from flask import render_template, request, redirect, url_for
import algorithms
app = Flask(__name__)

@app.route('/',methods=['GET'])
def sortviz():
    return render_template('index.html')


@app.route('/animation',methods=['POST'])
def animation():
    file_dict = {
            'quick' : 'quicksort.html',
            'bubble' : 'bubblesort.html',
            'insertion' : 'insertionsort.html'
            }
    file_list=[]

    if request.form.get('quick') == 'on':
        algorithms.QuickSort(file_dict['quick'])
        file_list.append(file_dict['quick'])

    if request.form.get('insertion') == 'on':
        algorithms.insertion_sort(file_dict['insertion']);
        file_list.append(file_dict['insertion'])

    if request.form.get('bubble') == 'on':
        algorithms.bubble_sort(file_dict['bubble']);
        file_list.append(file_dict['bubble'])

    return render_template('animation.html',fileList=file_list)
