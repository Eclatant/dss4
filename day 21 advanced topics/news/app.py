# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, jsonify, render_template, request, url_for, redirect

app = Flask(__name__)

'''
    Basic example
     - plain text
     - json
     - html
'''
@app.route('/txt_test')
def hello_plain():
    return 'plain text'

@app.route('/json_test')
def hello_json():
    data = {'name' : 'Aaron', 'family' : 'Byun'}
    return jsonify(data)

@app.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('simple.html')


@app.route('/simple')
def simple():
    # html file은 templates 폴더에 위치해야 함
    gadgets = []
    gadgets.append({'name' : 'galaxy s7', 'manufacturer' : 'samsung', 'date' : 2017})
    gadgets.append({'name' : 'macbook', 'manufacturer' : 'apples', 'date' : 2016})
    gadgets.append({'name' : 'action cam', 'manufacturer' : 'sony', 'date' : 2017})

    return render_template('simple2.html',
                                        name = 'aaron',
                                        age=32,
                                        languages = ['python', 'java', 'c++', 'c#'],
                                        gadgets = gadgets)

from pymongo import MongoClient, DESCENDING

@app.route('/simple_post', methods=['POST'])
def simple_post():
    name = request.form['name']
    age = request.form['age']

    print name, age

    mongo = MongoClient(host='54.149.163.97', port=27017)
    test = mongo.data2.test

    test.insert_one({'name' : name, 'age' : age})

    mongo.close()

    return redirect(url_for('index'))
    #return '이름 :  {} 나이 : {} 등록 완료'.format(name, age)

'''
    Complex Example
'''

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    try:
        mongo = MongoClient(host='54.149.163.97', port=27017)
        user = mongo.data2.user

        user.insert_one({'username' : username, 'password' : password})
        return render_template('register_complete.html')
    except:
        return render_template('register_error.html')
    finally:
        mongo.close()

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username_login']
    password = request.form['password_login']

    try:
        mongo = MongoClient(host='54.149.163.97', port=27017)
        user = mongo.data2.user

        doc = user.find_one({'username' : username})
        if doc:
            if doc['password'] == password:
                news = mongo.data2.news
                docs = []
                for doc in news.find().sort([('crawl_time', DESCENDING)]).limit(10):
                    item = {}
                    item['id']    = doc['_id']
                    item['title'] = doc['title']
                    item['category'] = doc['category']
                    item['crawl_time'] = doc['crawl_time']
                    docs.append(item)
                return render_template('news.html', news=docs)
            else:
                return render_template('login_error.html', message='비밀번호가 올바르지 않습니다.')
        else:
            return render_template('login_error.html', message='해당 사용자가 존재하지 않습니다.')
    except Exception, e:
        return render_template('login_error.html', message=str(e))
    finally:
        mongo.close()







        


@app.route('/news/search/<keyword>')
def search_news(keyword):
    try:
        mongo = MongoClient(host='54.149.163.97', port=27017)
        news = mongo.data2.news
        docs = news.find({'content' : {'$regex' : keyword}})

        result = []
        for doc in docs:
            item = {}
            item['id'] = doc['_id']
            item['title'] = doc['title']
            item['content'] = doc['content'][:100] + '...'
            item['category'] = doc['category']

            result.append(item)

        return render_template('news_search.html', news=result)
    except Exception, e:
        print e
    finally:
        mongo.close()

@app.route('/api/news/search/<keyword>')
def api_search_news(keyword):
    try:
        mongo = MongoClient(host='54.149.163.97', port=27017)
        news = mongo.data2.news
        docs = news.find({'content' : {'$regex' : keyword}})

        result = []
        for doc in docs:
            item = {}
            item['id'] = doc['_id']
            item['title'] = doc['title']
            item['content'] = doc['content']
            item['category'] = doc['category']
            result.append(item)

        return jsonify(result)
    except Exception, e:
        print e
    finally:
        mongo.close()


from konlpy.tag import Kkma
from collections import defaultdict
import numpy as np

@app.route('/news/similar_news_rt', methods=['POST'])
def similar_news():
    news_id = request.form['news_id']

    try:
        kkma = Kkma()

        mongo = MongoClient(host='54.149.163.97', port=27017)
        news = mongo.data2.news

        doc = news.find_one({'_id' : news_id})

        category = doc['category']
        doc_content = doc['content']
        doc_keyword = kkma.nouns(doc_content.decode('utf-8'))
        doc_keyword_dict = defaultdict(int)

        for kw in doc_keyword:
            kw = kw.encode('utf-8')
            cnt = doc_content.count(kw)
            doc_keyword_dict[kw] = cnt

        doc_norm = np.sum(np.array(doc_keyword_dict.values()) ** 2)

        max_similarity = -1
        most_similar_doc = None

        for n in news.find({'category' : category}):
            if n['_id'] == news_id:
                continue

            content = n['content']
            keyword = kkma.nouns(content.decode('utf-8'))
            keyword_dict = defaultdict(int)

            for kw in keyword:
                kw = kw.encode('utf-8')
                cnt = content.count(kw)
                keyword_dict[kw] = cnt

            dot_product = sum([v * doc_keyword_dict[k] \
                                            for k, v in keyword_dict.items() \
                                            if k in doc_keyword_dict])

            norm = np.sum(np.array(keyword_dict.values()) ** 2)

            similarity = dot_product / float(doc_norm * norm)
            print n['_id'], similarity, dot_product

            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_doc = n['_id']

        print max_similarity, most_similar_doc
        return render_template('similar_news.html', org_doc =news_id,
                                                similar_doc=most_similar_doc)
    except:
        pass
    finally:
        mongo.close()
        a = 1

@app.route('/news/category/<news_id>')
def categorize_news(news_id):
    pass

if __name__ == '__main__':
    # 모든 호스트에서 접속 가능
    # port : 8080, aws에서 8080을 열어줘야 접속 가능
    app.run(debug=True, host='0.0.0.0', port=8023)
