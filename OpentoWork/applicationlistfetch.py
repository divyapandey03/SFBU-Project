import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database configuration
mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="Google#009",
  database="open2work"
)

# Dummy authentication token
AUTH_TOKEN = "opentowork"

# Endpoint for getting list of applications
@app.route('/api/application/getList', methods=['POST'])
def get_application_list():
    # Check for valid token
    token = request.json.get('token')
    if not token or token != AUTH_TOKEN:
        return jsonify({'code': 401, 'msg': 'Unauthorized'}), 401
    
    # Get list of applications from database
    mycursor = mydb.cursor()
    mycursor.execute("SELECT  company_name, company_description, application_deadline, technical_assessment_deadline, interview_date, interview_from_to, application_status FROM Application")
    applications = []
    for row in mycursor.fetchall():
        application = {
            " company_name": row[0],
            "company_description": row[1],
            "application_deadline": row[2].strftime('%Y-%m-%dT%H:%M:%SZ'),
            "technical_assessment_deadline": row[3].strftime('%Y-%m-%dT%H:%M:%SZ'),
            "interview_date": row[4].strftime('%Y-%m-%dT%H:%M:%SZ'),
            "interview_from_to": row[5],
            "application_status": row[6]
        }
        applications.append(application)
    
    return jsonify({'code': 200, 'msg': 'ok', 'data': applications}), 200

if __name__ == '__main__':
     app.run( host='0.0.0.0', port=8080)
