from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello, World Get this Money</h1>'\
            '<p> This is a paragraph.</p>'



@app.route("/bye")
def say_bye():
    return "Peace"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == '__main__':
    app.run(debug=True)