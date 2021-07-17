from flask import abort
from app import db
import shop

class Monitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(20))

    shopid = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    shop = db.relationship("Shop", backref=db.backref("monitors", lazy=True))

    world = db.Column(db.String(10))
    size = db.Column(db.Integer)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    z = db.Column(db.Integer)

    def toDict(self):
        return {
            "name": self.name,
            "shop": self.shop.name,
            "world": self.world,
            "size": self.size,
            "x": self.x,
            "y": self.y,
            "z": self.z
        }


def createMonitor(name, shopName, world, size, x, y, z):
    s = shop.Shop.query.filter_by(name=shopName).first()
    if s == None:
        abort(404, "shop doesn't exist")
    
    monitor = Monitor(name=name, shop=s, world=world, size=size, x=x, y=y, z=z)
    db.session.add(monitor)
    db.session.commit()
    return monitor.toDict()


def getMonitors():
    return list(map(lambda m: m.toDict(), Monitor.query.all()))