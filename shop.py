from app import db
from flask import abort
from datetime import datetime
import player
import item

class ShopItems(db.Model):
    __tablename__ = "shop_item"
    shopid = db.Column(db.Integer, db.ForeignKey("shop.id"), primary_key=True)
    itemid = db.Column(db.Integer, db.ForeignKey("item.id"), primary_key=True)
    amount = db.Column(db.Integer)
    price = db.Column(db.Float)

    def toDict(self):
        return {
            
        } 


shop_owner = db.Table("shop_owner",
    db.Column("shopid", db.Integer, db.ForeignKey("shop.id"), primary_key=True),
    db.Column("playerid", db.Integer, db.ForeignKey("player.id"), primary_key=True)
)

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(50), nullable=False, default="")
    creation_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    items = db.relationship("ShopItems")
    owners = db.relationship("Player", secondary=shop_owner, lazy="subquery", backref=db.backref("shops", lazy=True))

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date.strftime("%d/%m/%Y %H:%M:%S"),
            "owners": list(map(lambda p: p.toDict(), self.owners))
        }
    
    def toDictAll(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date.strftime("%d/%m/%Y %H:%M:%S"),
            "owners": list(map(lambda p: p.toDict(), self.owners)),
            "items": list(map(lambda i: i.toDict(), self.items))
        }
    

def createShop(name, playerName, description=""):
    if name == "test":
        shop = Shop(name=name, description=description, id=-1, creation_date=datetime.utcnow())
        player.createPlayer(playerName)
        owner = player.Player.query.filter_by(name=playerName).first()
        shop.owners.append(owner)
        return shop.toDict()
    if Shop.query.filter_by(name=name).first() != None:
        abort(409, "Name is taken")

    shop = Shop(name=name, description=description)

    owner = player.getOrCreatePlayer(playerName)
    print(owner)
    shop.owners.append(owner)

    db.session.add(shop)
    db.session.commit()
    return shop.toDict()


def getShops():
    return list(map(lambda s: s.toDict(), Shop.query.all()))


def getShopById(id):
    s = Shop.query.filter_by(id=id).first()
    if s == None:
        abort(404)
    return s.toDict()
