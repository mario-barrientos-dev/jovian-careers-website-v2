from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def helloWord():
  greeting = "Hola Mundo"
  return render_template("home.html", context=greeting)

if __name__ == "__main__":
  app.run(
    host="0.0.0.0",
    debug=True,
  )
