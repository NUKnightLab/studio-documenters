import os
from flask import Flask, request
app = Flask(__name__)
from money import get_money_docs, DOCS_DIR
from flask import render_template


docs = get_money_docs()

@app.route('/')
def index():
    return render_template('index.html', docs=docs)


@app.route('/doc')
def doc():
    text = open(os.path.join(DOCS_DIR, request.args['doc'])).read().split('\n')
    return render_template('doc.html', text=text)

