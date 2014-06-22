from __future__ import with_statement

from . import app

app.testing = True
client = app.test_client()


def teardown_function(function):
    pass


def test_health():
    response = client.get('/health')
    assert b'OK' in response.data
