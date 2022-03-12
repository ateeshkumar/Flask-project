import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Document):
    user_id = db.IntField( unique = True)
    first_name = db.StringField( max_length = 50)
    last_name = db.StringField( max_length = 50)
    email = db.StringField( max_length = 50, unique = True)
    password = db.StringField( max_length = 50)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def get_password(self, password):
        self.password = check_password_hash(self.password, password)
        
class Course(db.Document):
    course_id = db.StringField( max_length = 50, unique = True)
    title = db.StringField( max_length = 50 )
    
    description = db.StringField( max_length = 50 )
    ppu = db.IntField()
    batters = db.StringField( max_length = 50 )

class Enrollment(db.Document):
    user_id = db.IntField()
    course_id = db.StringField( max_length = 50)
