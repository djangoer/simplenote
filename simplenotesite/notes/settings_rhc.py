import os
is_mysql=False
#dbpath=os.environ['OPENSHIFT_DATA_DIR']
MEDIA_ROOT = os.environ.get('OPENSHIFT_DATA_DIR', '')
if is_mysql:
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': 'ssc',
	        'USER': 'adminUQte5iE',
	        'PASSWORD': 'jCfBRsAW2nre',
	        'HOST': os.environ.get('OPENSHIFT_MYSQL_DB_HOST'),
	        'PORT': os.environ.get('OPENSHIFT_MYSQL_DB_PORT'),
	        'CONN_MAX_AGE': 600,
	    }
	}
