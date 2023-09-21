from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<p>Hello Hack Night!</p>"

@app.route("/<variable>")
def varpage(variable):
    # escape() used to ensure good input!
    return f"<p>Hello {escape(variable)}!</p>"

if __name__ == "__main__":
    app.run()
