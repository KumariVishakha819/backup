import flask

###Creating Flask Instance
app = flask.Flask(__name__)

@app.route("/")
def Home():
    return "I am brave"

@app.route("/<name>")
def User(name):
    return  f'Hello {name}  !'

@app.route("/admin")
def Administrator():
     return flask.redirect(flask.url_for("User" ,name="Hero"))

if __name__ == "__main__":
    app.run()

