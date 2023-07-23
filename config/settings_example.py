from settings import *

SECRET_KEY = 'your-secret-key'

DEBUG = True
TEST_MODE = False
API_DOCUMENTATION = True
DEBUG_TOOLBAR = True
TEMPLATES[0]['OPTIONS']['debug'] = True

HOST_PORT = '3668'
SITE = "%s://%s:%s" % (SITE_SCHEME, SITE_URL, HOST_PORT)

DATABASES['default']['PASSWORD'] = 'whatsnew-password'

if DEBUG_TOOLBAR:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
