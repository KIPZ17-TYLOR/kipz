from flask import app, render_template
from requests import request

def get_db_connection():
    def selected_date():


        @app.route('/balance_sheet', methods=['GET', 'POST'])
        def balance_sheet():
            selected_date = request.form.get('date') if request.method == 'POST' else None
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if selected_date:
        cursor.execute("SELECT * FROM Balance_Sheet WHERE date = %s", (selected_date,))
    else:
        cursor.execute("SELECT * FROM Balance_Sheet ORDER BY date DESC LIMIT 1")

    balance_data = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('balance_sheet.html', balance_data=balance_data, selected_date=selected_date)
