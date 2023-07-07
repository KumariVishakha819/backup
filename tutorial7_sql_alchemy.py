import flask
import flask_sqlalchemy


app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///user.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True

db = flask_sqlalchemy.SQLAlchemy(app)
class user(db.Model):
    _id_= db.Column("id",db.Integer,primary_key=True)
    name= db.Column(db.String(100))
    email= db.Column(db.String(100))

    def __init__(self,name,email):
        self.name=name
        self.email= email



@app.route("/",methods=["POST","GET"])
def home():
    if flask.request.method == "POST":
      name= flask.request.form["nm"]
      email = flask.request.form["em"]
      users= user(name,email)
      db.session.add(users)
      db.session.commit()
      return "<h1> User Added Successfully</h1>"
    else:
        return flask.render_template("db_form.html")
      




if __name__ =="__main__":
    
    app.ccreat
    app.run(debug=True)
    