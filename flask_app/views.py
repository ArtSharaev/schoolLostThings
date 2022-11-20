from flask_app import app
from flask import render_template, request, url_for
from os import listdir


def get_files(path) -> list:
    array = []
    full_path = "flask_app/static/" + path
    for filename in listdir(full_path):
        filename = path + "/" + filename
        array.append(filename)
    return array


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/B15-3', methods=['POST', 'GET'])
def b15_3():
    return render_template('building.html', building_name='B15-3',
                           photos=get_files("photos/B15-3"))


@app.route('/N19', methods=['POST', 'GET'])
def n19():
    return render_template('building.html', building_name='N19',
                           photos=get_files("photos/N19"))


@app.route('/BF15', methods=['POST', 'GET'])
def bf15():
    return render_template('building.html', building_name='BF15',
                           photos=get_files("photos/BF15"))


@app.route('/FB13-2', methods=['POST', 'GET'])
def fb13_2():
    return render_template('building.html', building_name='FB13-2',
                           photos=get_files("photos/FB13-2"))


@app.route('/FB3-2', methods=['POST', 'GET'])
def fb3_2():
    return render_template('building.html', building_building_name='FB3-2',
                           photos=get_files("photos/FB3-2"))
