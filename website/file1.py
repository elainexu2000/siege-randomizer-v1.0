from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello this is the Siege Randomizer </h1>"

"""
# Can treat string after web URL as a variable: http://127.0.0.1:5000/V
@app.route("/<name>")
def user(name):
    return f"Hello {name}!" # Hello V!

# redirects to home
@app.route("/admin/")
def admin():
    # url_for accepts name of the function, alongside the function's parameters
    return redirect(url_for("user", name = "Admin!!!")) 
"""

if __name__ == "__main__":
    app.run(debug=True)