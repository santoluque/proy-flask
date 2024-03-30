import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

app = Flask(__name__)

""" DB CONNECTION """
def db_connection():
    conn = sqlite3.connect('mydb.db')
    conn.row_factory = sqlite3.Row
    return conn

def find_client_by_id(cid):
    conn = db_connection()
    client = conn.execute('SELECT * FROM cliente WHERE id = ?',
                        (cid,)).fetchone()
    conn.close()
    if client is None:
        abort(404)
    return client


@app.route('/')
def index():
    conn = db_connection()
    clientes = conn.execute('SELECT * FROM cliente').fetchall()
    conn.close()
    return render_template('index.html',clientes=clientes)


@app.route('/<int:cid>')
def cliente(cid):
    cliente = find_client_by_id(cid)
    return render_template('client.html', cliente=cliente)