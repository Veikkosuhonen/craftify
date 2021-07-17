from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


def addItem(name):
    db.session.add(Item(name=name))
    db.session.commit()


def getOrCreateItem(name):
    i = Item.query.filter_by(name=name).first()
    if i == None:
        db.session.add(Item(name=name))
        db.session.commit()
        return Item.query.filter_by(name=name).first()
    else:
        return i