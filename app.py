from flask import Flask
from flask_restful import Api

from api.model.beer import Beer, BeerList, NewBeer

app = Flask(__name__)
api = Api(app)


api.add_resource(Beer, '/beer/<int:_id>')
api.add_resource(NewBeer, '/new-beer')
api.add_resource(BeerList, '/beers')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)