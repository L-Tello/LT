from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
import os


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def principal():
    return {"nombre":"Ludwin Tello", "carnet":"202010303"}

a
if __name__ == '__main__':
    puerto = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=puerto)






