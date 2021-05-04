from flask_restful import Resource
from ..database.connection import Connection

class Beer(Resource):
    def get(self, id):
        connection = Connection('stock.db')
        # id, name, style, price, stock
        if connection.insert("INSERT INTO beers VALUES (NULL, ?, ?, ?, ?)", ('Heiniken', 'lager', 10.99, 100)):
            return {'beer': {'name':'Heiniken', 'style':'lager', 'price':10.99, 'stock':100}}
        else
            return {'message':'Error try insert item in get method :D'}