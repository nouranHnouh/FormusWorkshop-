#import flask for webframework
from flask import Flask, render_template
from flask import request,redirect,url_for
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


@app.route("/topic/add",methods=["GET","POST"])
def topic_add():
	if request.method=='POST':
		#sending data to template 
		new_post=models.Post(request.form["title"],request.form["content"])
		post_store.add(new_post)
		return redirect(url_for("home")) 
	else:
		return render_template("topic_add.html")

 
if __name__ == "__main__":
	dummy_data.test(member_store,post_store)
	app.run(debug=True)
