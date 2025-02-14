from flask import session

def test_login(client):
    response = client.post('/auth/login', data={'username': 'flask'})
    assert response.status_code == 200
    with client:
        assert session['user_id'] == 1
