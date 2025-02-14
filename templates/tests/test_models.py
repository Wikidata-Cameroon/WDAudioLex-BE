from my_project.models import db, Post

def test_create_post(app):
    with app.app_context():
        post = Post(title='Test Post', content='This is a test post.')
        db.session.add(post)
        db.session.commit()

        assert post.id is not None
        assert post.title == 'Test Post'
