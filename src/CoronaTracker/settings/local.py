from django.conf import settings

# noinspection PyUnresolvedReferences
from .base import *

ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'tmp', 'db.sqlite3'),
    }
}
settings.ALLOWED_HOSTS = ALLOWED_HOSTS
