from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    users.append(data)
    return jsonify({'message': 'User created successfully'})

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(port=8081)
