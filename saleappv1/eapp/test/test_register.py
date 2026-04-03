from eapp.test.test_base import test_app, test_session
from eapp.dao import add_user
from eapp.models import User
import hashlib

def test_register(test_session):
    add_user(name='abc', username='demodemo', password='demo123456', avatar=None)

    u = User.query.filter(User.username.__eq__('demodemo')).first()

    assert u is not None
    assert u.name == 'abc'
    assert u.password == str(hashlib.md5('demo123456'.encode('utf-8')).hexdigest())