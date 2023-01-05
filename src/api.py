from unittest import result
from flask import Flask, jsonify, request
from language.langage import parse
from tools.Work import XmlToJson
import pprint

app = Flask(__name__)
 
@app.route('/api/find/', methods=['GET'])
def get_all_users():
    return jsonify(status="True")

@app.route('/api/find/<sentence>', methods=['GET'])
def get_one_users(sentence):
    if "FIND" in sentence:
        print(sentence)
        parse(sentence)
        res = XmlToJson()
        return jsonify(status="True", result = res)
    else: 
        return jsonify(status="false")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True) #enlver le debug

