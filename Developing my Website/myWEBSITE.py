# make a simple flask app

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)




@app.route('/')
def indexM():
    return render_template('index.html')

@app.route('/aboutme')
def index1():
    return render_template('aboutMe.html')





if __name__ == '__main__': 
    
    app.run(debug=True)