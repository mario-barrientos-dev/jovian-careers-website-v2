from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id":
    1,
    "title":
    "Data Analist",
    "location":
    "Bogota, Colombia",
    "description":
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla posuere mattis dui sit amet ullamcorper. Cras vitae vulputate nisl, eu.",
  },
  {
    "id":
    2,
    "title":
    "ML Engineer",
    "location":
    "Bucaramanga, Colombia",
    "description":
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla posuere mattis dui sit amet ullamcorper. Cras vitae vulputate nisl, eu.",
  },
  {
    "id":
    3,
    "title":
    "Backend Developer",
    "location":
    "Medellin, Colombia",
    "description":
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla posuere mattis dui sit amet ullamcorper. Cras vitae vulputate nisl, eu.",
  },
  {
    "id":
    4,
    "title":
    "FullStack Developer",
    "location":
    "Pasto, Colombia",
    "description":
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla posuere mattis dui sit amet ullamcorper. Cras vitae vulputate nisl, eu.",
  },
]


@app.route("/")
def helloWord():
  # greeting = "Hola Mundo"
  return render_template("home.html", jobs=JOBS, company_name="Slytherin")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(
    host="0.0.0.0",
    debug=True,
  )
