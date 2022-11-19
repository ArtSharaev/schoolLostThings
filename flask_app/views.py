from flask_app import app
from flask import render_template, request


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', name='MAIN')


@app.route('/B15-3', methods=['POST', 'GET'])
def b15_3():
    return render_template('index.html', name='B15-3')


@app.route('/N19', methods=['POST', 'GET'])
def n19():
    return render_template('index.html', name='N19')


@app.route('/BF15', methods=['POST', 'GET'])
def bf15():
    return render_template('index.html', name='BF15')


@app.route('/FB13-2', methods=['POST', 'GET'])
def fb13_2():
    return render_template('index.html', name='FB13-2')


@app.route('/FB3-2', methods=['POST', 'GET'])
def fb3_2():
    return render_template('index.html', name='FB3-2')
