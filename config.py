import mysql.connector

# Database configuration dictionary
db_config = {
    'host': 'localhost',
    'user': 'your_db_user',
    'password': '',
    'database': 'your_db_name'
}

def get_db_connection():
    """Establishes and returns a database connection."""
    return mysql.connector.connect(**db_config)
