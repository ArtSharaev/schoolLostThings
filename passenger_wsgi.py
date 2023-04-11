import sys

import os

INTERP = os.path.expanduser("/var/www/u2007038/data/lost/venv/bin/python")
if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from flask_app import application
