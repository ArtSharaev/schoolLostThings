from flask_app import app
from flask import render_template, request, url_for
from lib.funks import get_files


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/B15-3', methods=['POST', 'GET'])
def b15_3():
    return render_template('building.html',
                           building_name='Барклая, дом 15, к. 3 (𝟭𝟰𝟵𝟳)',
                           photos=get_files("photos/B15-3"))


@app.route('/N19', methods=['POST', 'GET'])
def n19():
    return render_template('building.html',
                           building_name='Новозаводская, дом 19 (𝟳𝟯𝟳)',
                           photos=get_files("photos/N19"))


@app.route('/BF15', methods=['POST', 'GET'])
def bf15():
    return render_template('building.html',
                           building_name='Большая Филевская, дом 15 (𝟳𝟐)',
                           photos=get_files("photos/BF15"))


@app.route('/FB13-2', methods=['POST', 'GET'])
def fb13_2():
    return render_template('building.html',
                           building_name='Филевский б-р, дом 13 к. 2 (𝟭𝟭𝟭𝟰)',
                           photos=get_files("photos/FB13-2"))


@app.route('/FB3-2', methods=['POST', 'GET'])
def fb3_2():
    return render_template('building.html',
                           building_name='Филевский б-р, дом 3 к. 2 (𝟭𝟭𝟭𝟰)',
                           photos=get_files("photos/FB3-2"))
