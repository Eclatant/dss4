# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, jsonify
from newsdao import NewsDAO
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def hello_json():
    data = {'name' : 'Aaron', 'family' : 'Byun'}
    return jsonify(data)

@app.route('/news/search/<keyword>')
def search_news(keyword):
    print type(keyword)
    newsdao = NewsDAO()
    data = newsdao.get_news_by_keyword_in_content(str(keyword))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)
