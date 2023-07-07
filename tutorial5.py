import flask


app = flask.Flask(__name__)
app.secret_key="Vishakha"

@app.route("/",methods=["POST","GET"])
def login():
    if flask.request.method == "POST":
        nm= flask.request.form["nm"]
        flask.session["test_user"]=nm
        return flask.redirect(flask.url_for("user" ))
    else:
        return flask.render_template("form.html")

@app.route("/test")
def test():
  if "test_user" in flask.session:
     test_user= flask.session["test_user"]
     return f'<h1>{test_user}</h1>'

@app.route("/user")
def user():
    if "test_user" in flask.session:
     test_user= flask.session["test_user"]
     return f"<p>Hello {test_user} </p>"

if __name__ =="__main__":
    app.run(debug=True)