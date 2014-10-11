import os
PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_DIR, 'sqlite_old.db'),  # Or path to database file if using sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Calcutta'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR,'..','static_root')
STATICFILES_DIRS = (os.path.join(PROJECT_DIR,'static'),)

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
#STATICFILES_DIRS = (
    #os.path.join(PROJECT_DIR,'..','..', 'static'),
    #os.path.join(path,'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'pzag*_q0n&^lajfpq^!gp)#60kz_&#j2y3w+r(e*h7u$c^ms#s'

# List of callables that know how to import templates from various sources.
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
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'notes.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'notes.wsgi.application'


# this will enable to call {{request.user}}
from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR,'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.humanize',
    #'django.contrib.markup',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'social_auth',
    'note',
    'registration',
    'userprofile',
    'crispy_forms',
    
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    #'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    #'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    #'social_auth.backends.contrib.disqus.DisqusBackend',
    #'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    #'social_auth.backends.contrib.orkut.OrkutBackend',
    #'social_auth.backends.contrib.foursquare.FoursquareBackend',
    #'social_auth.backends.contrib.github.GithubBackend',
    #'social_auth.backends.contrib.vk.VKOAuth2Backend',
    #'social_auth.backends.contrib.live.LiveBackend',
    #'social_auth.backends.contrib.skyrock.SkyrockBackend',
    #'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    #'social_auth.backends.contrib.readability.ReadabilityBackend',
    #'social_auth.backends.contrib.fedora.FedoraBackend',
    #'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TWITTER_CONSUMER_KEY         = 'oYJ7HIUoCXR6luGOF6M5NQ'
TWITTER_CONSUMER_SECRET      = 'c7EBWJkEQATKasVWLa83HvWmRuPYtOa2900feNRi40'
FACEBOOK_APP_ID              = '300242133500110'
FACEBOOK_API_SECRET          = '7d0b59cca13d5d56edeed5963e61261f'
LINKEDIN_CONSUMER_KEY        = 'n36y45tfip7i'
LINKEDIN_CONSUMER_SECRET     = 'px3cE9NlgrhDSTkp'
ORKUT_CONSUMER_KEY           = ''
ORKUT_CONSUMER_SECRET        = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = '47716508428.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = 'sRXUpoFRqMe4Fu686WKYq3ti'
FOURSQUARE_CONSUMER_KEY      = ''
FOURSQUARE_CONSUMER_SECRET   = ''
VK_APP_ID                    = ''
VK_API_SECRET                = ''
LIVE_CLIENT_ID               = '000000004C0F8E28'
LIVE_CLIENT_SECRET           = '75uS5WBYHZ9xCZGECbjXktHPlKmd7E7t'
SKYROCK_CONSUMER_KEY         = ''
SKYROCK_CONSUMER_SECRET      = ''
YAHOO_CONSUMER_KEY           = 'dj0yJmk9RXZLMVdVNTF1MVF1JmQ9WVdrOVNqRXlRM2xZTjJzbWNHbzlNVFEyTURFNE5qazJNZy0tJnM9Y29uc3VtZXJzZWNyZXQmeD1kYw--'
YAHOO_CONSUMER_SECRET        = '964ee9ee1d65615c8a784bb69c632a5089308c39'
READABILITY_CONSUMER_SECRET  = ''
READABILITY_CONSUMER_SECRET  = ''
GITHUB_APP_ID = 'fcd321fd035e7222093b'
GITHUB_API_SECRET = '329ffbb67ca69fe5abab6539901c7aaa62204e64'

FACEBOOK_EXTENDED_PERMISSIONS = ['email']
FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'ru_RU'}
LINKEDIN_SCOPE = ['r_basicprofile','r_emailaddress']
LINKEDIN_EXTRA_FIELD_SELECTORS = ['email-address']
LINKEDIN_EXTRA_DATA = [('id', 'id'),
                       ('first-name', 'first_name'),
                       ('last-name', 'last_name'),
                       ('email-address', 'email_address')]
TWITTER_EXTRA_DATA = [('email', 'email')]

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/?new=y'

SOCIAL_AUTH_ASSOCIATE_BY_MAIL = True
SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'social_auth.backends.pipeline.misc.save_status_to_session',
   # 'app.pipeline.redirect_to_basic_user_data_form'
)


ACCOUNT_ACTIVATION_DAYS = 7
SITE_URL='http://www.simplenote.in'

# gmail server settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'suhailvs@gmail.com'
EMAIL_HOST_PASSWORD = 'pnaoeogqwtqlgusd'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

LOGIN_ERROR_URL='/publicnote/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

on_webfaction=True
if on_webfaction:
    STATIC_URL = 'http://static.suhails.in/simplenote/'
    MEDIA_URL = STATIC_URL+'media/'
    STATIC_ROOT='/home/suhailvs/webapps/htdocs/simplenote/'
    MEDIA_ROOT = os.path.join(STATIC_ROOT,'media')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', 
            'NAME': 'simplenote',
            'USER': 'suhail',
            'PASSWORD': 'suhail',
            'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
            'PORT': '3306',
        }
    }

