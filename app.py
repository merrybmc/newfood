from pymongo import MongoClient
import jwt
import datetime
import hashlib
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

client = MongoClient(
    "mongodb+srv://h99:sparta@cluster2.cyd5okd.mongodb.net/?retryWrites=true&w=majority")
db = client.db


@app.route("/comment_list1", methods=["GET"])
def bucket_get1():
    info_list = list(db.comment_list1.find({}, {'_id': False}))
    return jsonify({'info': info_list})


@app.route("/comment_list2", methods=["GET"])
def bucket_get2():
    info_list = list(db.comment_list2.find({}, {'_id': False}))
    return jsonify({'info': info_list})


@app.route("/comment_list3", methods=["GET"])
def bucket_get3():
    info_list = list(db.comment_list3.find({}, {'_id': False}))
    return jsonify({'info': info_list})


@app.route("/comment_list4", methods=["GET"])
def bucket_get4():
    info_list = list(db.comment_list4.find({}, {'_id': False}))
    return jsonify({'info': info_list})


@app.route("/comment_list5", methods=["GET"])
def bucket_get5():
    info_list = list(db.comment_list5.find({}, {'_id': False}))
    return jsonify({'info': info_list})


@app.route("/comment_list6", methods=["GET"])
def bucket_get6():
    info_list = list(db.comment_list6.find({}, {'_id': False}))
    return jsonify({'info': info_list})


@app.route("/comment_list7", methods=["GET"])
def bucket_get7():
    info_list = list(db.comment_list7.find({}, {'_id': False}))
    return jsonify({'info': info_list})


@app.route("/comment_list1", methods=["POST"])
def bucket_post1():
    comment_receive = request.form['comment_give']
    comment_list = list(db.comment_list1.find({}, {'_id': False}))
    count = len(comment_list) + 1
    doc = {
        'num': count,
        'comment': comment_receive,
    }
    db.comment_list1.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})


@app.route("/comment_list2", methods=["POST"])
def bucket_post2():
    comment_receive = request.form['comment_give']
    comment_list = list(db.comment_list2.find({}, {'_id': False}))
    count = len(comment_list) + 1
    doc = {
        'num': count,
        'comment': comment_receive,
    }
    db.comment_list2.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})


@app.route("/comment_list3", methods=["POST"])
def bucket_post3():
    comment_receive = request.form['comment_give']
    comment_list = list(db.comment_list3.find({}, {'_id': False}))
    count = len(comment_list) + 1
    doc = {
        'num': count,
        'comment': comment_receive,
    }
    db.comment_list3.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})


@app.route("/comment_list4", methods=["POST"])
def bucket_post4():
    comment_receive = request.form['comment_give']
    comment_list = list(db.comment_list4.find({}, {'_id': False}))
    count = len(comment_list) + 1
    doc = {
        'num': count,
        'comment': comment_receive,
    }
    db.comment_list4.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})


@app.route("/comment_list5", methods=["POST"])
def bucket_post5():
    comment_receive = request.form['comment_give']
    comment_list = list(db.comment_list5.find({}, {'_id': False}))
    count = len(comment_list) + 1
    doc = {
        'num': count,
        'comment': comment_receive,
    }
    db.comment_list5.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})


@app.route("/comment_list6", methods=["POST"])
def bucket_post6():
    comment_receive = request.form['comment_give']
    comment_list = list(db.comment_list6.find({}, {'_id': False}))
    count = len(comment_list) + 1
    doc = {
        'num': count,
        'comment': comment_receive,
    }
    db.comment_list6.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})


@app.route("/comment_list7", methods=["POST"])
def bucket_post7():
    comment_receive = request.form['comment_give']
    comment_list = list(db.comment_list7.find({}, {'_id': False}))
    count = len(comment_list) + 1
    doc = {
        'num': count,
        'comment': comment_receive,
    }
    db.comment_list7.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})


@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        return render_template('page_Posts.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    nickname_receive = request.form['nickname_give']
    password_hash = hashlib.sha256(
        password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,
        "password": password_hash,
        "nickname": nickname_receive,  # 프로필 한 마디
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})


@app.route('/sign_up/check_dup2', methods=['POST'])
def check_dup2():
    nickname_receive = request.form['nickname_give']
    exists = bool(db.users.find_one({"nickname": nickname_receive}))
    return jsonify({'result': 'success', 'exists': exists})


@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one(
        {'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://merrybmc.shop/', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

one_p = soup.select_one('body > div.one > p').string
one_imgsrc = soup.find('div', 'one').find('img')['src']

two_p = soup.select_one('body > div.two > p').string
two_imgsrc = soup.find('div', 'two').find('img')['src']

three_p = soup.select_one('body > div.three > p').string
three_imgsrc = soup.find('div', 'three').find('img')['src']

four_p = soup.select_one('body > div.four > p').string
four_imgsrc = soup.find('div', 'four').find('img')['src']

five_p = soup.select_one('body > div.five > p').string
five_imgsrc = soup.find('div', 'five').find('img')['src']

six_p = soup.select_one('body > div.six > p').string
six_imgsrc = soup.find('div', 'six').find('img')['src']

seven_p = soup.select_one('body > div.seven > p').string
seven_imgsrc = soup.find('div', 'seven').find('img')['src']


@app.route('/order', methods=['GET'])
def view_orders():
    return jsonify({'one_p': one_p,
                    'one_is': one_imgsrc,
                    'two_p': two_p,
                    'two_is': two_imgsrc,
                    'three_p': three_p,
                    'three_is': three_imgsrc,
                    'four_p': four_p,
                    'four_is': four_imgsrc,
                    'five_p': five_p,
                    'five_is': five_imgsrc,
                    'six_p': six_p,
                    'six_is': six_imgsrc,
                    'seven_p': seven_p,
                    'seven_is': seven_imgsrc
                    })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5050, debug=True)
