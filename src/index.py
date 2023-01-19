from flask import Flask
from flask import request
from src import services

app = Flask(__name__)

@app.route('/v1/transpose', methods=['POST'])
def post_transpose_matrix():
    matrix = request.json
    if type(matrix) is list:
        transposed_matrix = services.transpose_matrix(matrix)
        return transposed_matrix
    return "Invalid matrix provided", 422