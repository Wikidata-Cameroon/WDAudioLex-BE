def test_get_posts(client):
    response = client.get('/posts')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_edit_user(client):
    response = client.post('/user/2/edit', data={
        'name': 'Flask',
        'theme': 'dark',
        'picture': (open('tests/resources/picture.png', 'rb'), 'picture.png')
    })
    assert response.status_code == 200
    assert b"User updated successfully" in response.data
