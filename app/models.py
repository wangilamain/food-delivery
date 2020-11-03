from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin,current_user

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique = True,index = False,nullable = False)
    email = db.Column(db.String(80),unique = True,index = False,nullable = False)
    bio = db.Column(db.String(255),default = 'My default Bio')
    hashed_password = db.Column(db.String(255),nullable = False)
    review = db.relationship('Review',backref = 'user',lazy = 'dynamic')
    order = db.relationship('Order',backref = 'user',lazy = 'dynamic')

    @property 
    def set_password(self):
        raise AttributeError('You cant read the password attribute')

    @set_password.setter
    def password(self,password):
        self.hashed_password = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.hashed_password,password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer,primary_key = True)
    food = db.Column(db.String(255),unique = True,nullable = False)
    cost = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    review = db.relationship('Review',backref = 'order',lazy = 'dynamic')
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_order(id):
        order = Order.query.filter_by(id=id).first()

        return order

    def __repr__(self):
        return f'Order {self.title}'

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer,primary_key = True)
    review = db.Column(db.String)
    posted = db.Column(db.DateTime,default = datetime.utcnow)
    order_id = db.Column(db.Integer,db.ForeignKey("orders.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    def get_review(id):
        review = Review.query.all(id=id)
        return review


    def __repr__(self):
        return f'Review {self.review}'

