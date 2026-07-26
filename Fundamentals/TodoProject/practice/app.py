from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():

    weeks = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    return render_template("index.html", 
                           name = "Deepak",
                           age = 30,
                           week = weeks) # **kwargs

if __name__ == "__main__":
    app.run(debug=True, port=8080)