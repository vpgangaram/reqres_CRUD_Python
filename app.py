from flask import Flask, jsonify, redirect, render_template, request, url_for
import requests

app = Flask(__name__)
BASE_URL = 'https://reqres.in/api/users'
array_of_delete_users = []

@app.route('/users', methods=["GET"])
def get_users():
    all_users = []
    for page_num in range(1, 4): 
        response = requests.get(BASE_URL + "?page=" + str(page_num))
        data = response.json().get('data', [])
        all_users.extend(data)
    return render_template('index.html',all_users = all_users, array_of_delete_users = array_of_delete_users)

@app.route('/users', methods=['POST'])
def create_user():
    data = {
        "name": request.form["name"],
        "job": request.form["job"],
    }
    response = requests.post(BASE_URL, json=data)
    return render_template('create_user.html', response=response.json())

@app.route('/users/<userId>', methods=['PUT'])
def update_user(userId):
    data = request.get_json()
    url = f'{BASE_URL}/{userId}'
    response = requests.put(url, json=data)
    return jsonify(response.json())

@app.route('/users/<int:userId>', methods=['GET'])
def delete_user(userId):
    url = f'{BASE_URL}/{userId}'
    requests.delete(url)
    array_of_delete_users.append(userId)
    return redirect(url_for('get_users'))  

if __name__ == '__main__':
    app.run(debug=True)
