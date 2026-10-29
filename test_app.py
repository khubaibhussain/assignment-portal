import pytest
from app import app, submissions

VALID = {
    'name': 'Ali Khan',
    'reg_no': 'FA22-BCS-001',
    'title': 'Lab 1',
    'url': 'https://github.com/ali/lab1',
}

@pytest.fixture
def client():
    app.config['TESTING'] = True
    submissions.clear()
    with app.test_client() as c:
        yield c

def test_valid_submission_is_saved_and_listed(client):
    r = client.post('/', data=VALID, follow_redirects=True)
    assert len(submissions) == 1
    assert b'Ali Khan' in r.data
    assert b'https://github.com/ali/lab1' in r.data

def test_missing_registration_number_is_rejected(client):
    r = client.post('/', data={**VALID, 'reg_no': ''}, follow_redirects=True)
    assert len(submissions) == 0
    assert b'Error' in r.data or b'required' in r.data.lower()

def test_invalid_url_is_rejected(client):
    r = client.post('/', data={**VALID, 'url': 'not-a-url'}, follow_redirects=True)
    assert len(submissions) == 0
    assert b'Invalid' in r.data or b'Error' in r.data