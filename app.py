from flask import Flask, render_template

# Create the Flask app with custom static and template folders
app = Flask(__name__, static_folder="static", template_folder="templates")

# Home route
@app.route("/")
def home():
    return render_template("index_flask.html")

# Projects route
@app.route("/projects")
def projects():
    return render_template("projects_flask.html")

if __name__ == "__main__":
    # Run the app in debug mode locally
    app.run(debug=True)

