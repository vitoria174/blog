from flask import Flask,render_template

app = Flask(__name__)

lista=['oi','ola']

@app.route('/home')
def home():
      return render_template("home.html")

app.run()