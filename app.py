from flask import Flask, render_template, request

from src.codevecdb.parse_code import parseCodeAndInsert
from src.codevecdb.search_code import searchCode
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/code', methods=['GET', 'POST'])
def post_code():
    if request.method == 'POST':
        codestr = request.form['code']
        results = parseCodeAndInsert(codestr)
        return render_template('code.html', results=results)
    return render_template('code.html')


@app.route('/query', methods=['GET', 'POST'])
def query_code():
    if request.method == 'POST':
        query = request.form['query']
        results = searchCode(query)
        return render_template('query.html', results=results)
    return render_template('query.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        with open(os.path.join('uploads', file.filename), 'r') as f:
            content = f.read()
            print(content)
        return render_template('upload_file.html', content=content)
    return render_template('upload_file.html')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello code vector db!'


if __name__ == '__main__':
    app.run()
