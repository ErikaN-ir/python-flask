import os
from flask import Flask #importing flask class

app = Flask(__name__) #Creating an instance of it & storing it in app
#__name__ is the name of the module - built-in python variable
@app.route("/") #wraps a function
def index():
    return "Hello, World"

if __name__ == "__main__": #name of default module
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)