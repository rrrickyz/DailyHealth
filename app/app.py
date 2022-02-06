from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

import routes

if __name__ == '__main__':
    app.run(debug=True)
