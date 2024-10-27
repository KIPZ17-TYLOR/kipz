from flask import app, flash, redirect, render_template, url_for
from pydantic import MySQLDsn
from requests import request, session
import mysql.connector
from mysql.connector import Error

@app.route('/add_stock', methods=['GET', 'POST'])

def add_stock():
    # Ensure the user is logged in
    if 'user_id' not in session:
        flash("Please log in to add stock.", "danger")
        return redirect(url_for('login'))

    if request.method == 'POST':
        try:
            product_id = request.form['product_id']
            quantity = int(request.form['quantity'])

            def get_db_connection():
            # Database connection
                conn = get_db_connection()
            cursor = conn.cursor()

            # Update product stock and log addition
            cursor.execute("UPDATE Products SET quantity_in_stock = quantity_in_stock + %s WHERE product_id = %s",
                           (quantity, product_id))
            cursor.execute("INSERT INTO Stock_Additions (product_id, quantity_added, added_by, date_added) VALUES (%s, %s, %s, NOW())",
                           (product_id, quantity, session['user_id']))
            conn.commit()

            flash("Stock added successfully.", "success")

        except MySQLDsn.connector.Error as err:
            flash(f"Database error: {err}", "danger")

        except ValueError:
            flash("Quantity must be an integer.", "danger")

        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('dashboard'))



    # Fetch products for dropdown selection
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('add_stock.html', products=products)
