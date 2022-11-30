from flask import Flask, render_template, g, request, session, flash, url_for, redirect
import sqlite3

DATABASE = "banco.bd"
SECRET_KEY = "1234"

app = Flask("Olá mundo")

app.config.from_object(__name__)

def conectar():
    return sqlite3.connect(DATABASE)

@app.before_request 
def before_request():
    g.bd = conectar()

@app.teardown_request
def teardown_request(f):
    g.bd.close()

@app.route("/")
def exibir_posts():
    sql  = "SELECT titulo, texto, data_criacao FROM posts ORDER BY id DESC" 
    resultado = g.bd.execute(sql)
    posts = []

    for titulo, texto, data_criacao in resultado.fetchall():
        posts.append({
            "titulo": titulo,
            "texto": texto,
            "data_criacao": data_criacao
        })
    return render_template("exibir_posts.html", post = posts)

@app.route("/login", methods = ["POST", "GET"])
def login():
    erro = None
    if(request.method == "POST"):
        if request.form['username'] == "Ocean" and request.form['password'] == "ocean1234":
            session['logado'] = True
            flash("Usuario logado " + request.form['username'])
            return redirect(url_for('exibir_posts'))
        erro = "Usuário ou senha incorretos"    
    return render_template("login.html", erro=erro)    

@app.route("/logout")
def logout():
    session.pop('logado', None)    

    flash("Logout Efetuado")
    return redirect(url_for('exibir_posts'))
