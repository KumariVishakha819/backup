import flask


app = flask.Flask(__name__)


@app.route("/",methods=["POST","GET"])
def login():
    if flask.request.method == "POST":
        nm= flask.request.form["nm"]
        return flask.redirect(flask.url_for("user" ,usr=nm))
    else:
        return flask.render_template("form.html")


@app.route("/<usr>")
def user(usr):
     return f"<p>Hello {usr} </p>"

if __name__ =="__main__":
    app.run(debug=True)