import requests
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin

from news import get_articles

app = Flask(__name__)

CORS(app)

@app.route('/',methods=["GET"])
def home():
    return render_template('home.html')

@app.route('/dash',methods=["GET"])
def dash():
    return render_template('dash.html')


@app.route('/search',methods=["POST"])
def search():
    data=request.get_json()
    query=data['query']
    print(query)
    articles=get_articles(query=query)
    return articles
    
        
        
        
        
    



if( __name__ =='__main__'):
    app.run(debug=True)