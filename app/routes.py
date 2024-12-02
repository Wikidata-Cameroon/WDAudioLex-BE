from flask import jsonify, request
from .extensions import db
from .models import User, Post

def register_routes(app):
    @app.route('/users', methods=['GET'])
    def get_users():
        users = User.query.all()
        return jsonify([
            {
                'id': user.id, 
                'username': user.username, 
                'email': user.email
            } for user in users
        ])

    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.json
        new_user = User(username=data['username'], email=data['email'])
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({
            'id': new_user.id, 
            'username': new_user.username, 
            'email': new_user.email
        }), 201

    @app.route('/posts', methods=['POST'])
    def create_post():
        data = request.json
        new_post = Post(
            title=data['title'], 
            content=data['content'], 
            user_id=data['user_id']
        )
        
        db.session.add(new_post)
        db.session.commit()
        
        return jsonify({
            'id': new_post.id, 
            'title': new_post.title
        }), 201