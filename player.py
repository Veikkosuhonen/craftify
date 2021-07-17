from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name
        }

def createPlayer(name):
    if Player.query.filter_by(name=name) == None:
        db.session.add(Player(name=name))
        db.session.commit()

def getOrCreatePlayer(name):
    p = Player.query.filter_by(name=name).first()
    if p == None:
        db.session.add(Player(name=name))
        db.session.commit()
        return Player.query.filter_by(name=name).first()
    else:
        return p
    