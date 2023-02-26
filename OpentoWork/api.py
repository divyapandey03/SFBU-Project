
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# User database
users = [{'email': 'sfbu@gmail.com', 'password': 'testpassword'}]

# Sign up endpoint
@app.route('/signup', methods=['POST'])
def sign_up():
    data = request.get_json()
    email = data['email']
    password = data['password']

    # Check if user already exists
    if any(user['email'] == email for user in users):
        return make_response(jsonify({'message': 'Username already exists'}), 409)

    # Add new user to database
    users.append({'email': email, 'password': password})
    return make_response(jsonify({'message': 'User created successfully'}), 201)

# Log in endpoint
@app.route('/login', methods=['POST'])
def log_in():
    data = request.get_json()
    email = data['email']
    password = data['password']

    # Check if user exists
    user = next((user for user in users if user['email'] == email), None)
    if not user:
        return make_response(jsonify({'message': 'Invalid username or password'}), 401)
      
      
       # Check if password is correct
    if user['password'] != password:
        return make_response(jsonify({'message': 'Invalid username or password'}), 401)

    # Log user in
    return make_response(jsonify({'message': 'Logged in successfully'}), 200)

# Reset password endpoint
@app.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data['email']
    password = data['password']

    # Check if user exists
    user = next((user for user in users if user['email'] == email), None)
    if not user:
        return make_response(jsonify({'message': 'User not found'}), 404)

    # Reset password
    user['password'] = password
    return make_response(jsonify({'message': 'Password reset successfully'}), 200)
  
  # User database
users = []

# Register endpoint
@app.route('/api/user/register', methods=['POST'])
def register():
    # Get data from request
    data = request.get_json()
    fullName = data['fullName']
    email = data['email']
    password = data['pwd']

    # Check if user already exists
    if any(user['email'] == email for user in users):
        return make_response(jsonify({'code': 409, 'msg': 'Email already exists', 'data': None, 'token': None}), 409)

    # Add new user to database
    users.append({'fullName': fullName, 'email': email, 'password': password})
    token = generate_token(email) # generate token for user

    # Return success response
    return make_response(jsonify({'code': 200, 'msg': 'Congratulations, User Created Successfully!!!', 'data': None, 'token': token,}), 200)

# Generate token for user
def generate_token(email):
    # You can use any library or algorithm to generate token
    # For example, using UUID4 as token
    import uuid
    return str(uuid.uuid4())

if __name__ == '__main__':

   app.run( host='0.0.0.0', port=8080)

                                               
