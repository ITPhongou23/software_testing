import pytest

from eapp.test.test_base import test_app, test_session, moc_cloudinary
from eapp.dao import add_user
from eapp.models import User
import hashlib

def test_register(test_session):
    add_user(name='abc', username='demodemo', password='demo123456', avatar=None)

    u = User.query.filter(User.username.__eq__('demodemo')).first()

    assert u is not None
    assert u.name == 'abc'
    assert u.password == str(hashlib.md5('demo123456'.encode('utf-8')).hexdigest())

@pytest.mark.parametrize('password', [
    '1','1'*8,'a'*8,'1a1'*2
])
def test_invalid_password(password,test_session):
    with pytest.raises(ValueError):
        add_user(name='abc', username='demodemo', password=password, avatar=None)

def test_existing_username(test_session):
    add_user(name='abc', username='demodemo', password='demo123456', avatar=None)

    with pytest.raises(ValueError):
        add_user(name='abc', username='demodemo', password='demo123456', avatar=None)

def test_avatar(test_session, moc_cloudinary):
    add_user(name='abc', username='demodemo', password='demo123456', avatar='aaa')

    u = User.query.filter(User.username.__eq__('demodemo')).first()

    assert u is not None
    assert u.name == 'abc'
    assert u.password == str(hashlib.md5('demo123456'.encode('utf-8')).hexdigest())
    assert u.avatar == 'https:/fake_image.png'