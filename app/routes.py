from flask import Blueprint, render_template, current_app
from .extensions import db
from .models import User, Post

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """
    Home route for the application.

    This route does two things:
    1. Prints the list of templates available to Flask. This is useful for debugging and checking which templates Flask can find in the environment.
    2. Renders the 'index.html' template with a dynamic 'title' variable, which is passed from the route.

    The 'title' variable is used to set the page's title in the HTML head and can also be used within the page content.

    ---
    responses:
        200:
            description: Successfully rendered the index.html template with a dynamic title.
            content:
                text/html:
                    schema:
                        type: string
                        example: "<html> ... Welcome to WDAudioLEx ... </html>"
    """
    # Print the list of available templates Flask can find
    print(current_app.jinja_env.list_templates())  # This lists all templates Flask can find

    # Render the index.html template
    return render_template('index.html', title="Welcome to WDAudioLEx")

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
