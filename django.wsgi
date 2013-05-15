import os
import sys

sys.path.append('/home/helios/kaio-helios/helios-server')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
