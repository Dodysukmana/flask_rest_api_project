 # app/config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Pass_190798@localhost/api_cakrawala_diskusi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
