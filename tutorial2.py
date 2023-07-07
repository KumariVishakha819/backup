import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("child.html", content=["Daksh","Vishakha"])


if __name__=="__main__":
    app.run()

