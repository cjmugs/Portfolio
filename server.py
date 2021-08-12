# My Portfolio Site

from flask import Flask, render_template, url_for, request, redirect

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



@app.route("/data.html", methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
       data = request.form.to_dict()
       print(data)
       return redirect("/data.html")
    else:
        return "something went wrong, try again"

@app.route("/download.html")                       
def download():
    return render_template('download.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')