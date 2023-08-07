from sqlalchemy import create_engine, text

url = "mysql+pymysql://8j6gv5vcluf4r2pbxntp:pscale_pw_RnvEJlGDuTGRHjfNTTNURiphkh266iPZx6GWq4s5Pbu@aws.connect.psdb.cloud/slytheryngcareers"
engine = create_engine(url,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})
