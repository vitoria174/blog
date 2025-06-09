from flask import Flask,render_template,request,redirect,url_for
from sessaoadmin import Article

artigo =Article()
app = Flask(__name__)

@app.route('/')
def home():
      ler = artigo.read_article()
      return render_template("home.html",titulo = "Artigos", lista=ler)

@app.route('/novo')
def criar():
      return render_template('criar_artigos.html',titulo_novo_artigo= 'Novo Artigo')

@app.route('/criar_artigo', methods = ['POST',])
def criar_artigo():
      titulo = request.form['titulo']
      descricao = request.form['descricao']
      art = artigo.create_article(titulo,descricao)

      return redirect(url_for('home'))

app.run(debug= True)