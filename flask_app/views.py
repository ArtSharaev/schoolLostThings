from flask_app import application
from flask import render_template, request, url_for
from tools.tools import get_files


@application.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@application.route('/B15-3', methods=['POST', 'GET'])
def b15_3():
    return render_template('building.html',
                           building_name='Барклая, дом 15, к. 3',
                           building_num='1497',
                           photos=get_files("photos/B15-3"))


@application.route('/N19', methods=['POST', 'GET'])
def n19():
    return render_template('building.html',
                           building_name='Новозаводская, дом 19',
                           building_num='737',
                           photos=get_files("photos/N19"))


@application.route('/BF15', methods=['POST', 'GET'])
def bf15():
    return render_template('building.html',
                           building_name='Большая Филёвская, дом 15',
                           building_num='72',
                           photos=get_files("photos/BF15"))


@application.route('/FB13-2', methods=['POST', 'GET'])
def fb13_2():
    return render_template('building.html',
                           building_name='Филёвский б-р, дом 13, к. 2',
                           building_num='1114',
                           photos=get_files("photos/FB13-2"))


@application.route('/FB3-2', methods=['POST', 'GET'])
def fb3_2():
    return render_template('building.html',
                           building_name='Филёвский б-р, дом 3, к. 2',
                           building_num='1114',
                           photos=get_files("photos/FB3-2"))
