from flask import abort
from app import db
import shop
import player
import item
import timestamps

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    shopid = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    shop = db.relationship("Shop", backref=db.backref("transactions", lazy=True))

    playerid = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    player = db.relationship("Player", backref=db.backref("transactions", lazy=True))

    itemid = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    item = db.relationship("Item", backref=db.backref("transactions", lazy=True))

    amount = db.Column(db.Integer, nullable=False)
    timeStamp = db.Column(db.DateTime, nullable=False)

    def toDict(self):
        return {
            "shop": self.shop.name,
            "player": self.player.name,
            "item": self.item.name,
            "amount": self.amount,
            "timeStamp": timestamps.getIsoFormat(self.timeStamp)
        }


def createTransaction(shopName, playerName, material, amount, timeStamp):
    s = shop.Shop.query.filter_by(name=shopName).first()
    if s == None:
        abort(404, "shop doesn't exist")
    p = player.getOrCreatePlayer(playerName)
    i = item.getOrCreateItem(material)
    transaction = Transaction(shop=s, player=p, item=i, amount=amount, timeStamp=timeStamp)
    db.session.add(transaction)
    db.session.commit()
    return transaction.toDict()