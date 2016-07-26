"""
WSGI config for sie project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

### these 2 lines are used to run the monitor.py ##
import site1.monitor
site1.monitor.start(interval=1.0)
###


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site1.settings")

application = get_wsgi_application()

