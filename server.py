# Min for a FLask server to work 

from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route("/")                       
def home_page():
    return render_template('index.html')

@app.route("/index.html")                       
def home():
    return ('Home Homie')

@app.route("/about.html")                       
def about():
    return ('Thats what Im about')

@app.route("/projects.html")                       
def projects():
    return ('Projecting Projects')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')