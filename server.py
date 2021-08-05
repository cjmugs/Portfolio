# My Portfolio Site

from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route("/index.html")                       
def home_page():
    return render_template('index.html')

@app.route("/about.html")                       
def about():
    return render_template('about.html')

@app.route("/projects.html")                       
def projects():
    return render_template('projects.html')
    
@app.route("/contact.html")                       
def contact():
    return render_template('contact.html')

@app.route("/download.html")                       
def download():
    return render_template('download.html')

@app.route("/data.html")                       
def data():
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')