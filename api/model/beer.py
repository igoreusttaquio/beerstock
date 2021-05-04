from flask_restful import Resource
from flask import request
from ..database.connection import Connection

class Beer(Resource):
    def get(self, _id):
        connection = Connection('stock.db')
        row = connection.find("SELECT * FROM beers WHERE id=?", (_id,), True)
        connection.close()
        return {'beer':{'name' : row[1], 'style':row[2], 'price':row[3], 'stock':row[4]}}
    

    def put(self, _id):
        connection = Connection('stock.db')
        data  = request.get_json()
        name  = data['name']
        style = data['style']
        price = data['price']
        stock = data['stock']
        
        beer = connection.update("UPDATE beers SET name=?, style=?, price=?, stock=? WHERE id=?", 
        (name, style, price, stock, _id))
        connection.commit()
        connection.close()

        return {'message' : f'Beer {name} has been updated.'}, 201



class NewBeer(Resource):
    def post(self):
        connection = Connection('stock.db')
        data  = request.get_json()
        name  = data['name']
        style = data['style']
        price = data['price']
        stock = data['stock']
        # id, name, style, price, stock
        if connection.insert("INSERT INTO beers VALUES (NULL, ?, ?, ?, ?)", (name, style, price, stock)):
            connection.commit()
            connection.close()
            return {'beer': {'name': name, 'style': style, 'price': price, 'stock': stock}}, 201
        else:
            return {'message':'Error try insert item.'}, 404


class BeerList(Resource):
    def get(self):
        connection = Connection('stock.db')
        all_beers = []
        result = connection.find_all("SELECT * FROM beers")
        if result:
            for row in result:
                all_beers.append({
                    'id' : row[0], 
                    'name':row[1],
                    'style':row[2],
                    'price':row[3],
                    'stock':row[4]
                })
            connection.close()
            return {'beers':all_beers}, 200
        connection.close()
        return {'beers' : []}, 404