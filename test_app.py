import pytest
import app


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    client = app.app.test_client()
    yield client


def test_client_page(client):
    rv = client.get('/')
    # Main page (instructions)
    assert b'<p class="lead">A Pusher-powered chat application built using Flask</p>' in rv.data
    # Chat window
    assert b'<input type="email" class="form-control" id="email" placeholder="Email Address*" required>' in rv.data


def test_adminpage(client):
    rv = client.get('/admin')
    # Admin page (0 connected clients)
    assert b'Select a chat window to show and sent messages to' in rv.data


# Selenium script with clients interacting with the admin
