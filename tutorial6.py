import flask

app= flask.Flask(__name__)
app.secret_key="vishakha"

@app.route("/")
def Home():
    flask.flash("Home Sweet Home")
    return flask.render_template("flash.html")

if __name__=="__main__":
    app.run(debug=True)