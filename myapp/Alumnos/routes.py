from flask import Blueprint

alumnos=Blueprint('alumnos', __name__)

@alumnos.route('/getAlumn', methods=['GET', 'POST'])
def getAlumn():
    return {'key':'Alumnos'}