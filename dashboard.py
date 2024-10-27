from multiprocessing.connection import Connection
from sqlite3 import connect
from flask import app, render_template
from numpy import conj
def get_db_connection():


    @app.route('/dashboard', methods=['GET'])
    def dashboard():
        conn = get_db_connection()
    cursor = connect.cursor(dictionary=True)

    # Get all products and their stock levels
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    cursor.close()
    Connection.close()

    return render_template('dashboard.html', products=products)
