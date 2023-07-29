import requests
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
from algo import return_summary



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
    url=data['url']
    text=data['box']
    if url!= None:
        pass
    
    if text !=None:
        try:
            summary=return_summary(text)
            return [summary]
        except:
            return ["error"]
    
    return "hello"
    
        
@app.route('/results',methods=["GET"])
def results():
    return render_template('results.html')
        
        
    



if( __name__ =='__main__'):
    app.run(debug=True)