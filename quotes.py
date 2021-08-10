from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:Hetero@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://qznbxjzyajjczj:90bdd79a80e2040d1f7ea15ed715d2a511916ee4a94306d737729449430fc6dc@ec2-44-194-145-230.compute-1.amazonaws.com:5432/dd65nl58hj68pe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False  #event notification system. takes alot of resources

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)
    #fruits = ["apple","grapes","berries","oranges"]
    #return render_template('index.html', quote='Kindness needs no translation',fruits=fruits)

#@app.route('/about')
#def about():
    #return '<h1> Hello World from about page</h1>'

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process',methods =['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata =Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index')) #chaged from index.gtml to index so it will return the view function
