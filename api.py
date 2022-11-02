from unittest import result
from flask import Flask, jsonify, request
from markupsafe import escape

app = Flask(__name__)
 
@app.route('/api/find/', methods=['GET'])
def get_all_users():
    return jsonify(status="True")

@app.route('/api/find/<test>', methods=['GET'])
def get_one_users(test):
    return jsonify(status="True", result = {'find': test})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)