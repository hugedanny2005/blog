"""
WSGI config for site1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site1.settings")

application = get_wsgi_application()

###### Detect Daemon mode or Embedded mode ########
# import sys

# def application(environ, start_response):
# 	status = '200 OK'

# 	if not environ['mod_wsgi.process_group']:
# 		output = 'EMBEDDED MODE'
# 	else:
# 		output = 'DAEMON MODE'

# 	response_headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(output)))]

# 	start_response(status, response_headers)

# 	return [output]