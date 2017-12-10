### DONE BY NARENDREN S

import requests
import json
import sys
from flask import Flask,render_template,make_response, request, send_from_directory
from werkzeug.routing import Rule

app=Flask(__name__)

    

### TASK 1 ###
@app.route('/')
def hello_world():
   return 'Hello World - Narendren'


### TASK 2 ###    
def authorcount():
    r=requests.get('https://jsonplaceholder.typicode.com/users')
    print(r.text)
    j=r.text
    users=json.loads(j)


    r=requests.get('https://jsonplaceholder.typicode.com/posts')
    print(r.text)
    j=r.text
    posts=json.loads(j)
    k=0
    d={}
    for i in range(len(users)):
        u=users[i]
        id=u['id']
        print(id)
        count=0
        print(posts[k]['userId'])
        while (posts[k]['userId']==id):
            count=count+1
            k=k+1
            if k==len(posts):
                break

        d[u['name']]=count  
        print(count)

    return d
    
@app.route("/authors")
def log():
    return render_template("printdict.html",dict=authorcount())
    


### TASK 3 ###
@app.route('/home')
def home():
    return render_template('home.html');

@app.route('/setcookie',methods=['POST','GET'])
def setcok():
    if len(request.cookies)==0 and request.method=='POST':
        n=request.form['name']
        a=request.form['age']
        resp=make_response(render_template('setcookie.html'))
        resp.set_cookie('name',n)
        resp.set_cookie('age',a)
        return resp
    else:
        return "Already "+ str(len(request.cookies))+" cookies are set"

### TASK 4 ###
@app.route('/getcookie')
def getcok():
    n=request.cookies.get('name')
    a=request.cookies.get('age')
    return "<table style='border: 1px solid'><tr><td>Name "+n+"</td></tr><tr><td>Age "+a+"</td></tr></table>"


### TASK 5 ###
@app.route('/robots.txt')
def deny():
    return render_template('error.txt'), 400, {'Content-Type': 'text/plain'}


### TASK 6 ###
import os
@app.route('/image')
def image():
    return send_from_directory(os.path.join(app.root_path, 'templates'),'img.jpg', mimetype='image/jpeg')


### TASK 7 ###
@app.route('/input')
def data():
    return render_template('input.html')

app.url_map.add(Rule('/postdata', endpoint='op'))
@app.endpoint('op')
def example():
    sys.stdout.write(request.form['d']+'\n')
    return "Logged received data: "+request.form['d']

@app.route('/postdata',methods=['POST'])
def index():
    return 1


if __name__=="__main__":
    app.run()

sys.stdout.close()
