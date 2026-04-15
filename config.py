import os
import urllib.parse
import pyodbc

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key-fallback-for-local-dev'

    SQL_SERVER = os.environ.get('SQL_SERVER')
    SQL_DATABASE = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')
    # For Azure SQL, using the official ODBC Driver is recommended.
    # The following logic detects if Driver 18 is available, falling back to 17.
    _drivers = pyodbc.drivers()
    _driver = '{ODBC Driver 18 for SQL Server}' if 'ODBC Driver 18 for SQL Server' in _drivers else '{ODBC Driver 17 for SQL Server}'

    _odbc_conn_str = (
        'DRIVER=' + _driver + ';'
        'SERVER=' + (SQL_SERVER or '') + ';'
        'PORT=1433;'
        'DATABASE=' + (SQL_DATABASE or '') + ';'
        'UID=' + (SQL_USER_NAME or '') + ';'
        'PWD=' + (SQL_PASSWORD or '') + ';'
        'Encrypt=yes;'
        'TrustServerCertificate=yes;'
    )
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(_odbc_conn_str)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER')

    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    AUTHORITY = os.environ.get('AUTHORITY')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"

