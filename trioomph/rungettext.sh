#!/bin/sh
PATH=$PATH:/usr/local/opt/gettext/bin/ django-admin.py makemessages -l en
PATH=$PATH:/usr/local/opt/gettext/bin/ django-admin.py makemessages -l fr
PATH=$PATH:/usr/local/opt/gettext/bin/ django-admin.py compilemessages 
