import pandas as pd
import pyodbc as pdb
from flask import Flask, request, jsonify
from flask_cors import CORS

### Connect to SQL Server database ###
# Connect to SQL Server database info
SERVER = 'DUYNGUYEN\SQLEXPRESS'
DATABASE = 'Project'
USERNAME = 'sa'
PASSWORD = '123456'

# Connection string
connectionString = f'''
DRIVER={{ODBC Driver 18 for SQL Server}};
SERVER={SERVER};DATABASE={DATABASE};
UID={USERNAME};
PWD={PASSWORD};
Encrypt=no;
'''

# Connect to SQL Server
conn = pdb.connect(connectionString)


### Utility functions ###
# Username, password & email validation must be done in frontend!
def register_user(user):
    username = user.get('username')
    password = user.get('password')
    user_id = user.get('user_id')
    email = user.get('email')
    user_type = user.get('user_type')

    # User_id validation
    select_query = f"""
    SELECT * FROM User_info
    WHERE User_info.user_id = {user_id}
    OR User_info.username = '{username}';
    """
    cursor = conn.cursor()
    cursor.execute(select_query)
    records = cursor.fetchall()
    msg = jsonify({'success': False})
    if len(records) > 0:
        msg = jsonify({'success': False})
    else:
        # Insert user info into User_info table
        insert_query = f"""
        INSERT INTO User_info VALUES ({user_id}, '{username}', '{password}', '{email}', {user_type})
        """
        cursor.execute(insert_query)
        conn.commit()
        msg = jsonify({'success': True})
    return msg

def login_user(user):
    username = user.get('username')
    password = user.get('password')
    query = 'SELECT * FROM User_info WHERE username = ? AND user_password = ?'
    cursor = conn.cursor()
    cursor.execute(query, username, password)
    user = cursor.fetchone()

    if user:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Invalid username or password'})

def get_user_info(id):
    query = 'SELECT * FROM User_info WHERE user_id = ?'
    cursor = conn.cursor() 
    cursor.execute(query, id)
    user = cursor.fetchone()
    return jsonify(user)

### Server communication ###
app = Flask(__name__)
CORS(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    msg = register_user(data)
    return msg

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    msg = login_user(data)
    return msg

@app.route('/getUserInfo', methods=['GET'])
def getUserInfo():
    data = request.get_json()
    info = get_user_info(data)
    return info


# Start server
if __name__ == '__main__':
    app.run(debug=True)

