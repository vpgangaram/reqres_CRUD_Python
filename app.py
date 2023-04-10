from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/users', methods=["GET"])
def get_users():
    url = 'https://reqres.in/api/users'
    response = requests.get(url)
    return jsonify(response.json())

@app.route('/users', methods=['POST'])
def create_user():
    url = 'https://reqres.in/api/users'
    data = request.json
    response = requests.post(url, json=data)
    return jsonify(response.json())

@app.route('/users/<userId>', methods=['PUT'])
def update_user(userId):
    url = f'https://reqres.in/api/users/{userId}'
    data = request.json
    response = requests.put(url, json=data)
    return jsonify(response.json())

@app.route('/users/<userId>', methods=['DELETE'])
def delete_user(userId):
    url = f'https://reqres.in/api/users/{userId}'
    response = requests.delete(url)
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True)
