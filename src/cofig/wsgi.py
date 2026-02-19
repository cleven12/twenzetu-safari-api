"""
WSGI config for cofig project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application

# Add the src directory to the path — required when running from PythonAnywhere's
# /var/www/ wsgi.py location (which is outside the project directory).
_src_dir = Path(__file__).resolve().parent.parent
if str(_src_dir) not in sys.path:
    sys.path.insert(0, str(_src_dir))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cofig.settings')

application = get_wsgi_application()

