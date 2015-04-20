# TURN ON THE VIRTUAL ENVIRONMENT FOR YOUR APPLICATION
activate_this = '/home/<username>/.virtualenvs/rango/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
import sys

# ADD YOUR PROJECT TO THE PYTHONPATH FOR THE PYTHON INSTANCE
path = '/home/<username>/tango_with_django/tango_with_django_project'

if path not in sys.path:
    sys.path.append(path)

os.chdir(path)

# TELL DJANGO WHERE YOUR SETTINGS MODULE IS LOCATED
os.environ['DJANGO_SETTINGS_MODULE'] = 'tango_with_django_project.settings'

# IMPORT THE DJANGO WSGI HANDLER TO TAKE CARE OF REQUESTS
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
