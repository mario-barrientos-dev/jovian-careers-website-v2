from sqlalchemy import create_engine, text

url = "mysql+pymysql://2705ah0zplrgxv206xje:pscale_pw_itP5kmEVLDfsJqzBlhLd7U2O1aoCVo16xUiQr4q2sQO@aws.connect.psdb.cloud/slytheryngcareers"
engine = create_engine(url,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


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
    print(jobs)

    return jobs
