from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder="static", template_folder=".")

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Projects route
@app.route("/projects")
def projects():
    return render_template("projects.html")

# Static files (if needed for serving additional assets dynamically)
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True)
