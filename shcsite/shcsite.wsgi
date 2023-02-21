import os
import sys

project_dir = '/home/ubuntu/shcsite'
sys.path.insert(0, project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'shcsite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
