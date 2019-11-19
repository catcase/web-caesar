from caesar import caesar
from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form methods="POST">
        <label for="rot">
        Rotate by:
        <input type="text" name="rot" value="0"/>
        </label>
        <textarea name="text"></textarea>
        <input type="submit" value="Encrypt Me"/>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt(rot, caesar):
    return caesar

@app.route("/")
def index():
    return form

app.run()