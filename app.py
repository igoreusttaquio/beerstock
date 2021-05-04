from flask import Flask
from flask_restful import Api

from api.model.beer import Beer

app = Flask(__name__)
api = Api(app)


api.add_resource(Beer, '/beer/<int:id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)