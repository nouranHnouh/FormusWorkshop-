#import flask for webframework
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
@app.route("/index")
def home():
    return "Hi there"
    
@app.route("/sayhello/<name>/")
def sayhello(name):
    return "Hello {}".format(name)
 
if __name__ == "__main__":
    app.run()
