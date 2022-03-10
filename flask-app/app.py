from application import app
from application import db
from application.models import User, Recipe 

db.drop_all()
db.create_all()

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)