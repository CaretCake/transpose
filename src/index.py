"""Api for transposing matrices."""

from flask import Flask
from flask import request
from src import services

app = Flask(__name__)

@app.route('/v1/transpose', methods=['POST'])
def post_transpose_matrix():
    matrix = request.json
    if type(matrix) is list and type(matrix[0]) is list:
        try:
            transposed_matrix = services.transpose_matrix(matrix)
            return transposed_matrix
        except ValueError:
            return 'Failed to transpose - matrix size is likely incorrect', 422
    return 'Invalid input provided', 422