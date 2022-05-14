from .base import *
from .security import SECRET_KEY

SECRET_KEY = SECRET_KEY
DEBUG = False

try:
    from .local import *
except ImportError:
    pass
