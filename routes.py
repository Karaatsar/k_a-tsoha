from db import db
from app import app
from flask import render_template, request, redirect
import messages, users

@app.route("/")
def etusivu():
    list = categories.get_list()
    count_messages = messages.get_counter()
    return render_template("etusivu.html", list==list, count_messages=count_messages)
    
@app.route("/kirjaudu", methods=["GET", "POST"])
def kirjaudu():
    if request.method == "GET":
       return render_template("kirjaudu.html")
    if request.method == "POST":
       username = request.form["username"]
       password = request.form["password"]
       if users.kirjaudu(username, password):
            return redirect("/")
       else:
            return render_template("error.html", message="Annoit väärän tunnuksen tai salasanan")
            
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/sisään", methods=["GET", "POST"])
def sisaan():
    if request.method == "GET":
       return render_template("sisään.html")
    if request.method == "POST":
       username = request.form["username"]
       password1 = request.form["password_1"]
       password2 = request.form["password_2"]
       if password1 != password2:
          return render_template("error.html", message="Annoit kaksi eri salasanaa")
       if users.sisaan(username, password1):
          return redirect("/")
       else:
          return render_template("error.html", message="Rekistöröinti ei onnistunut")
