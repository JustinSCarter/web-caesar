from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

encrypt_form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
            form {{
                 background-color: #eee;
                 padding: 20px;
                 margin: 0 auto;
                 width: 540px;
                 font: 16px sans-serif;
                 border-radius: 10px;
            }}
            textarea {{
                 margin: 10px 0;
                 width: 540px;
                 height: 120px;
            }}
            </style>
        </head>
    <body>
        <form method="POST">
        <label for="rot"> Rotate by: </label>
        <input type="text" name="rot" value=0 id="rot">
        <input type="submit" value="Encrypt my text!">
        <textarea name="text" id="text"> {encrypted_text} </textarea>
    </body>
 </html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']

    rot = int(rot)
    text = rotate_string(text, rot)
    return encrypt_form.format(encrypted_text=text)

@app.route("/",)
def index():
    return encrypt_form.format(encrypted_text='')

app.run()
