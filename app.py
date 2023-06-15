from flask import Flask, render_template, request

from src.codevecdb.parse_code import parseCodeAndInsert
from src.codevecdb.search_code import searchCode, getAllCode
from src.codevecdb.split.split_dispatch import split_file_to_function
from src.codevecdb.milvus_vectordb import create_connection
    
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
create_connection()


@app.route('/code', methods=['GET', 'POST'])
def post_code():
    if request.method == 'POST':
        code_str = request.form['code']
        results = parseCodeAndInsert(code_str)
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
        split_file_to_function(file)
        return render_template('upload_file.html')
    return render_template('upload_file.html')


@app.route('/')
def hello_world():
    results = getAllCode()
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run()
