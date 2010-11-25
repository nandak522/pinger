import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('NandaKishore', 'madhav.bnk@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pinger',                      # Or path to database file if using sqlite3.
        'USER': 'pinger',                      # Not used with sqlite3.
        'PASSWORD': 'pinger',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Asia/Calcutta'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

ROOT_PATH = os.getcwd()

PROJECT_DIRECTORY_NAME = ROOT_PATH.split(os.sep)[-1]  

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

MEDIA_ROOT = '%s/site_media/' % ROOT_PATH

MEDIA_URL = ''

EMAIL_SUBJECT_PREFIX = '[%s] ' % PROJECT_DIRECTORY_NAME.capitalize()

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'o27y($=t1yh#(^tnuz2vkzds1cs48=*=*e*foi*x^4jz)v#+eh'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = '%s.urls' % PROJECT_DIRECTORY_NAME

TEMPLATE_DIRS = (
    '%s/templates' % ROOT_PATH,
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'domains'
)

IS_PROXY_CONNECTION = False
if IS_PROXY_CONNECTION:
    PROXY_SETTINGS = {'username':'validusername',
                      'password':'password',
                      'host':'192.168.1.1',
                      'port':'9999'}
else:
    PROXY_SETTINGS = {}