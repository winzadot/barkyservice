# the simplest flask application can fit in a single source file
from enum import unique
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.util import join

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def p_wrap(line):
    return f"<p>{line}</p>"


def li_wrap(item):
    return f"<li>{item}</li>"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
        nullable=False)
    category = db.relationship('Category',
        backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name


def db_init():
    # if the database doesn't exist, create it an all associated entities
    db.drop_all()
    db.create_all()

    # Create Users
    admin = User(username='admin', email='admin@awesome.xyz')
    guest = User(username='guest', email='guest@awesome.xyz')

    db.session.add(admin)
    db.session.add(guest)

    # Create Posts and Categories
    cat_py = Category(name="Python")

    # this is a very interesting aspect of sqlalchemy: the relationship between category and post
    # means that objects associated with a category through a relationships are also added
    # when the category is added/committe
    Post(title="Hello Python!", body="Python is greate", category=cat_py)

    # here is a direct addition to the category
    my_post = Post(title="My life with snakes", body="Good times")

    # the posts list is a back reference/query to any posts related to this category
    cat_py.posts.append(my_post)

    # add all to the database by adding the category
    db.session.add(cat_py)

    # Save it all
    db.session.commit()    


##### ROUTES #####
@app.route("/")
def homepage():
    output = User.query.all()
    app.logger.debug(output)

    # show users
    show = p_wrap(f"username 1: {output[0].username} | username 2: {output[1].username}")
    show += f"<hr>"

    # show posts and categories
    query = Category.query.options(joinedload('posts'))
    for category in query:
        show += "<ul>"
        show += li_wrap(f"{category.name}")
        for post in category.posts:
            show +="<ul>"
            show += li_wrap(f"{post.title}")
            show +="</ul>"
        
        show +="</ul>"

    show += f"<hr>"
    
    return str(show)


if __name__ == '__main__':
    db_init()
    app.run(debug=True)