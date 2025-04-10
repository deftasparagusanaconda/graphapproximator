# when you do "import graphapproximator", it imports this directory as a module
# this __init__.py file will convert that from a module to an instance of Engine
# graphapproximator then becomes an instance/module hybrid
# the instance exposes the modules using dot notation (e.g. ga.interpolators)

from .engine import Engine

# spawn the default instance
_instance = Engine()

# make the package itself behave like an instance of Engine
# i got this code from AI, please dont berate me
def __getattr__(name):
    return getattr(_instance, name)

def __setattr__(name, value):
    return setattr(_instance, name, value)

def __dir__():
    return dir(_instance)

# replace the module import with the instance
from sys import modules
modules[__name__] = _instance
