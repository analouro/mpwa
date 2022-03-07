from application import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    recipe_name = db.Column(db.String(100), nullable=False) 
    recipes = db.relationship('Recipe', backref='userbr')

class Recipe(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(100), nullable=False)
    fuser_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    # recipe_ing = db.Column(db.String(500), nullable=True)
    # recipe_servs = db.Column(db.Integer, nullable=True)
    # recipe_guide = db.Column(db.String(2000), nullable=True)


