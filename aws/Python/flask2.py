from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def head():
    first = "Bu benim ilk condition tecrübem"
    return render_template("index.html", message = first)
app.route("/vincenzo")
def mylist():
    names = ["A", "aha", "mike"]
    return render_template("body.html",)
if __name__=="__main__":
        #app.run(debug=True, port=5000)
        app.run(host='0.0.0.0', port=80)
        
    