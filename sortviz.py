#!/usr/bin/env python3

#Checks whether depencies are installed and installs if missing
import sys
import subprocess
import glob

try:
    import matplotlib
except:
    print("matplotlib not installed, installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])

try:
    import celluloid
except:
    print("celluloid not installed, installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "celluloid"])

try:
    import flask
except:
    print("flask not installed, installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])

try:
    import bjoern
except:
    print("matplotlib not installed, installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "bjoern"])

#Actual app starts from here
import os
import algorithms
import webbrowser
from random import shuffle
# from threading import Timer
from flask import Flask, render_template, request, redirect, url_for

#Suppresses all the flask clutter in terminal
import logging
os.environ['WERKZEUG_RUN_MAIN'] = 'true'

app = Flask(__name__)

#Disables template caching which leads to the same array being used for sorting everytime
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/',methods=['GET'])
def sortviz():
    random_array = list(range(1,11))
    shuffle(random_array)
    return render_template('index.html',names = algorithms.pretty_names(),array=" ".join(list(map(str,random_array))))


@app.route('/animation',methods=['POST'])
def animation():
    array = list(map(int,request.form.get('array').strip().split()))

    function_names = algorithms.function_names()
    filenames = algorithms.filenames()
    chosen=[]

    for algo in function_names:
        if request.form.get(algo) == 'on':
            function_names[algo](array.copy(),filenames[algo])
            chosen.append(filenames[algo])

    return render_template('animation.html',fileList=chosen)

@app.errorhandler(500)
def error(e):
    return render_template('error.html'),500

# opens browser automatically
def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == "__main__":  
    # Timer(1, open_browser).start()
    bjoern.run(app,'0.0.0.0',5000)
    # app.run(host='0.0.0.0', port=5000)
    toremove = glob.glob(os.path.join(sys.path[0],'templates','*sort.html'))
    for _file in toremove:
        os.remove(_file)
