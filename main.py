from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)
api = Api(app)

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def get(self):
        return f'<User {self.username, self.password}>'
    
user_args = reqparse.RequestParser()

user_args.add_argument("username", type=str, required=True)
user_args.add_argument("password", type=str, required=True)

class UserList(Resource):

    def post(self):
        args = user_args.parse_args()

        user_id = len(user.query.all()) + 1

        new_user = user(id=user_id, username=args["username"], password=args["password"])
        db.session.add(new_user)
        db.session.commit()

        return new_user, 201

api.add_resource(UserList, '/users')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)