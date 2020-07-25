from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from . import db

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), index = True)
    email = db.Column(db.String(250), unique=True, index=True)
    password_hash = db.Column(db.String(400))
    blog_id = db.relationship('Blog', backref='user', lazy='dynamic')
    review_id = db.relationship('Review', backref='user', lazy='dynamic')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('Access Denied!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.username}'



class Role(db.Model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    role = db.Column(db.String)
    user = db.relationship('User', backref='role', lazy='dynamic')


    def __repr__(self):
        return f'User {self.name}'




class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    blog = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.now(tz=None))
    review_id = db.relationship('Review', backref='blog', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_blog(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_blog(cls, id):
        blogs = Blog.query.order_by(Blog.posted.desc()).all()
        return blogs

    @classmethod
    def delete_blog(self, blog_id):
        reviews = Review.query.filter_by(blog_id=blog_id).delete()
        blog = Blog.query.filter_by(id=blog_id).delete()
        db.session.commit()

    @classmethod
    def edit_blog(self, blog_id):

        blog = Review.query.filter_by(id=blog_id).edit()

        db.session.commit()



class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)

    review = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.now(tz=None))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls, id):
        reviews = Review.query.filter_by(blog_id=id).all()
        return reviews

    @classmethod
    def delete_review(self, review_id):

        review = Review.query.filter_by(id=review_id).delete()

        db.session.commit()

class Subscribers(db.Model):
    __tablename__ = "subscribers"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, index = True)
    
    def __repr__(self):
        return f"Subscribers('{self.email}')"
    
    
class Quote:
    """
    Blueprint class for quotes consumed from API
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote