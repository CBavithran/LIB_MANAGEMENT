import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:cbavithran02102003@localhost/lib_package'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Make sure to replace 'username' and 'password' with actual database credentials.
