#import flask for webframework
from flask import Flask, render_template
import models
import stores
import dummy_data
app = Flask(__name__)
member_store=stores.Memberstore()
post_store=stores.Poststore()
@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html',posts=post_store.get_all())
#@app.route("/sayhello/<name>/")
#def sayhello(name):
    #return "Hello {}".format(name)

 
if __name__ == "__main__":
	dummy_data.test(member_store,post_store)
	app.run(debug=True)
