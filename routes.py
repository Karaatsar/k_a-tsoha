from db import db
from app import app
from flask import render_template, request, redirect, session
import messages, users

@app.route("/")
def frontpage():
    print("ETUSIVULLA OLLAAN")
    print("user_id" in session)
     username = users.get_username(session["user_id"])
        message_list = messages.get_list()
        return render_template("frontpage.html", username=username, messages=message_list)
    else:
        return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
       return render_template("login.html")
    if request.method == "POST":
       username = request.form["username"]
       password = request.form["password"]
       if users.login(username, password):
            print("kirjautuminen onnistui")
            return redirect("/")
       else:
            return render_template("error.html", message="Annoit väärän tunnuksen tai salasanan")  
               
@app.route("/logout")
def logout(): 
    users.logout()
    return redirect("/")
    #del session["user_id"]
    #return redirect("/")


@app.route("/inside", methods=["GET", "POST"])
def inside():
    if request.method == "GET":
        return render_template("inside.html")
    if request.method == "POST":
       username = request.form["username"]
       password1 = request.form["password_1"]
       password2 = request.form["password_2"]
       if password1 != password2:
          return render_template("error.html", message="Annoit kaksi eri salasanaa")
       if users.register(username, password1):
          return redirect("/")
       else:
          return render_template("error.html", message="Rekistöröinti ei onnistunut")
          
@app.route("/chain1")
def chain1():
    if "user_id" in session: 
        username = users.get_username(session["user_id"])
        ketju_messages = messages.get_ketju_messages("chain1")
        count_messages = len(ketju_messages)
        return render_template("chain1.html", username=username, messages=ketju_messages, count=count_messages)
    else:
       return redirect("/login")

@app.route("/chain2")
def chain2():
    if "user_id" in session: 
        username = users.get_username(session["user_id"])
        ketju_messages = messages.get_ketju_messages("chain2")
        count_messages = len(ketju_messages)
        return render_template("chain2.html", username=username, messages=ketju_messages, count=count_messages)
    else:
       return redirect("/login")

@app.route("/chain3")
def chain3():
    if "user_id" in session: 
        username = users.get_username(session["user_id"])
        ketju_messages = messages.get_ketju_messages("chain3")
        count_messages = len(ketju_messages)
        return render_template("chain3.html", username=username, messages=ketju_messages, count=count_messages)
    else:
       return redirect("/login")

@app.route("/new", methods=["GET", "POST"])
def new():
    if "user_id" in session:
       if request.method == "GET":
            username = users.get_username(session["user_id"])
            return render_template("new.html", username=username)
       elif request.method == "POST":
            return redirect("/")
    else:
       return redirect("/login")   

@app.route("/send", methods=["POST"])
def send_message():
    if "user_id" in session:
        content = request.form["content"]
        if messages.send_message(content): 
            return redirect("/")
        else:
            return render_template("error.html", message="Viestin lähetys ei on>
