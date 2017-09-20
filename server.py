from flask import Flask, render_template, request
from os import path
import shelve

app = Flask(__name__)
db = shelve.open(path.join(app.root_path, 'shelve.db'), writeback=True)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=["POST"])
def submit():
    message = request.form['message']
    db.setdefault('messages', [])
    db['messages'].append(message)
    return render_template('done.html', submitted=True)


@app.route('/view')
def view():
    db.setdefault('messages', [])
    messages = db['messages']
    return render_template('show-all-messages.html', messages=messages)


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port='5000'
    )
