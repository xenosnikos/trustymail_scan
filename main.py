from flask import Flask
from flask_restful import Api

from controllers.trustymail_api import TrustyMail

app = Flask(__name__)
api = Api(app)

api.add_resource(TrustyMail, "/v2/trustyMail")

if __name__ == "__main__":
    app.run()
