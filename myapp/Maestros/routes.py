from flask import Blueprint

maestros=Blueprint('maestros', __name__)

@maestros.route('/getMaes', methods=['GET', 'POST'])
def getMaes():
    return {'key':'Maestros'}