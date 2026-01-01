from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html", title="Calendar")

@app.route("/activities")
def activities():
    return render_template("activities.html")

@app.route("/vision")
def vision():
    return render_template("vision.html")

@app.route("/members")
def members():
    return render_template("members.html")

@app.route("/recruit")
def recruit():
    return render_template("recruit.html")

if __name__ == "__main__":
    app.run(debug=True)
