from flask import request
from flask_restful import Resource, Api
from app import app

import shop
import transaction
import monitor

api = Api(app)


class ShopResource(Resource):
    def get(self, id):
        return shop.getShopById(id)
    
    
class ShopListResource(Resource):
    def get(self):
        return shop.getShops()
    
    def post(self):
        data = request.json
        print(data)
        newShop = shop.createShop(data["name"], data["playerName"], data["description"])
        return newShop


class TransactionListResource(Resource):
    def get(self):
        return transaction.getTransactions()
    
    def post(self):
        data = request.json
        print(data)
        newTransaction = transaction.createTransaction(data["shop"], data["player"], data["item"], data["amount"], data["timeStamp"])
        return newTransaction


class MonitorListResource(Resource):
    def get(self):
        return monitor.getMonitors()
    
    def post(self):
        data = request.json
        print(data)
        newMonitor = monitor.createMonitor(data["name"], data["shop"], data["world"], data["size"], data["x"], data["y"], data["z"])
        return newMonitor


api.add_resource(ShopResource, "/api/shops/<shopid>")
api.add_resource(ShopListResource, "/api/shops")

api.add_resource(TransactionListResource, "/api/transactions")

api.add_resource(MonitorListResource, "/api/monitors")