from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False) 
    recipes = db.relationship('Recipe', backref='user')

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # recipe_ing = db.Column(db.String(500), nullable=True)
    # recipe_servs = db.Column(db.Integer, nullable=True)
    # recipe_guide = db.Column(db.String(2000), nullable=True)

# db.create_all()


