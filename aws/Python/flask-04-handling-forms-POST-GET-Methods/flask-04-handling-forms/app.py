import re
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('main.html', name ="Cevat")
@app.route('/greet', methods=['GET'])
def greet():
    if 'user' in request.args:
        myname = request.args['user']
        return render_template("greet.html", user=myname)
    else:
        return render_template("greet.html", user = "Send your username with 'user' parameter in ?")



@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        myname = request.form['username']
        cipher = request.form['password']
        if cipher == "123":
            return render_template("secure.html", user=myname.title())
        else:
            return render_template("login.html", user=myname.title(), control = True)
    else:
        return render_template("login.html", control = False)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
        