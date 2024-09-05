from flask import Blueprint

apiUser= Blueprint('usertest', __name__, url_prefix='/usertest')

@apiUser.post('/<user>')
def testUser(user):
    return user