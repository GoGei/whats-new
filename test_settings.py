from default_settings import *

SECRET_KEY = 'test'
TEST_RUNNER = os.environ.get("TEST_RUNNER", "django.test.runner.DiscoverRunner")

DEBUG = True
TEST_MODE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_TEST_NAME', 'whatsnew'),
        'USER': os.environ.get('DATABASE_TEST_USER', 'whatsnew'),
        'PASSWORD': os.environ.get('DATABASE_TEST_PSW'),
        'HOST': os.environ.get('DATABASE_TEST_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_TEST_PORT', 5432),
        'ATOMIC_REQUESTS': True,
        'TEST': {
            'NAME': os.environ.get('DATABASE_TEST_NAME', 'whatsnew_test'),
        }
    }
}
