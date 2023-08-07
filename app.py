from flask import Flask, render_template, jsonify
from sqlalchemy import text
from database import engine

app = Flask(__name__)


def load_jobs_from_db():
  with engine.connect() as conn:
    results = conn.execute(text("select * from jobs"))
    column_names = results.keys()  # Obtener los nombres de las columnas
    jobs = []

    for row in results.all():
      result_dict = dict(
        zip(column_names,
            row))  # Combinar nombres de columna con valores de la fila
      jobs.append(result_dict)

    return jobs


@app.route("/")
def helloWord():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs, company_name="Slytherin")


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(
    host="0.0.0.0",
    debug=True,
  )
