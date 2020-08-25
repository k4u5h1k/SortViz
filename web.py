import random
import algorithms
from flask import Flask
from flask import render_template, request, redirect, url_for
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/',methods=['GET'])
def sortviz():
    return render_template('index.html',names = algorithms.pretty_names())


@app.route('/animation',methods=['POST'])
def animation():

    array = list(range(1,int(request.form.get('size'))+1))
    random.shuffle(array)


    file_list=[]

    function_names = algorithms.function_names()
    filenames = algorithms.filenames()

    for algo in function_names:
        if request.form.get(algo) == 'on':
            function_names[algo](array.copy(),filenames[algo])
            file_list.append(filenames[algo])

    return render_template('animation.html',fileList=file_list,rand=random.randint(0,1000))
