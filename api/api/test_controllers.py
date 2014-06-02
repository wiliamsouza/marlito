from __future__ import with_statement

from . import app

app.testing = True
app.config['WTF_CSRF_ENABLED'] = False
client = app.test_client()


def teardown_function(function):
    pass


def test_ping():
    response = client.get('/ping')
    assert b'Pong' in response.data


"""
def test_add_car():
    car_data = {'year': '1938', 'manufacturer': 'Volkswagen',
                'model': 'Beetle'}
    r = client.post('/users', data=user_data, follow_redirects=True)
    assert b'Thanks for registering' in r.data
    res = login('jhon@doe.com', 'jJdD')
    assert b'You were logged in' in res.data
    with open('cars/data/photo.jpg', 'rb') as f:
        car_data['photo'] = f
        response = client.post('/cars', data=car_data, follow_redirects=True)
        assert b'New car added' in response.data
"""
