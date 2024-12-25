from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder=".")

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Projects route
@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True)
