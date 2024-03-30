from flask import Flask

""" Instanciado aplicacion flask"""
""" __name__ -> variable del modulo actual de Python"""
app = Flask(__name__)

""" @app.route decorador de flask para mapear a funcion de flask """
@app.route('/')
def welcome():
    return 'Hola, Santiago'