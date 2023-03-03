from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Define the database connection parameters
DATABASE = 'your_database_name'
USER = 'your_database_user'
PASSWORD = 'your_database_password'
HOST = 'your_database_host'
PORT = 'your_database_port'

# Define a function to connect to the database
def get_db():
    conn = psycopg2.connect(
        dbname=DATABASE,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
    return conn

@app.route('/api/application/getList', methods=['POST'])
def getList():
    # Get the token from the request
    token = request.json.get('token')
    
    # Perform token authentication
    if token == 'your_secret_token':
        try:
            # Connect to the database
            conn = get_db()
            cur = conn.cursor(cursor_factory=RealDictCursor)
            
            # Execute the SQL query to get the application list
            cur.execute("SELECT * FROM application")
            data = cur.fetchall()
            
            # Close the database connection
            cur.close()
            conn.close()
            
            # Return the JSON response
            return jsonify({"code": 200, "msg": "ok", "data": data})
        
        except Exception as e:
            # Return the JSON response with an error message
            return jsonify({"code": 500, "msg": str(e)})
    
    else:
        # Return the JSON response with an error message
        return jsonify({"code": 401, "msg": "unauthorized"})

if __name__ == '__main__':
    app.run(debug=True)
