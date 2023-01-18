from flask import Flask
app = Flask(__name__)


@app.route("/transpose", methods=['GET'])
def get_transposed_matrix():
    return "hello!"
