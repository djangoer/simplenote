import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'notes.settings'

virtenv =os.path.join(os.environ['HOME'],'webapps','simplenote','myenv','bin','activate_this.py')
#virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtenv, dict(__file__=virtenv))
except IOError:
    pass

from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()
