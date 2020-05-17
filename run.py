import os
from flask import Flask, render_template #importing flask class

app = Flask(__name__) #Creating an instance of it & storing it in app
#__name__ is the name of the module - built-in python variable

@app.route("/") #wraps a function
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__": #name of default module
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
