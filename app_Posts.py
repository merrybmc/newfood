from pymongo import MongoClient
import jwt
import datetime
import hashlib
import requests
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
app = Flask(__name__)

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

# @app.route('/')
# def toy_project():
#     return render_template('page_Posts.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5050, debug=True)
