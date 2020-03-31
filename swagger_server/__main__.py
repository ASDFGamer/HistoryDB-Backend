#!/usr/bin/env python3

import connexion
from flask_sqlalchemy import SQLAlchemy

from swagger_server import encoder
from swagger_server.constants import NAME_MAX_LENGHT

app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'HistoryDB API'}, pythonic_params=True)
db = SQLAlchemy(app.app)


def main():
    app.run(port=8080)


if __name__ == '__main__':
    main()
