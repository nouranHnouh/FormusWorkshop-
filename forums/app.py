#import flask for webframework
from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')
#@app.route("/sayhello/<name>/")
#def sayhello(name):
    #return "Hello {}".format(name)
 
if __name__ == "__main__":
    app.run(debug=True)
