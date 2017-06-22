import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "multiscorer",
    version = "0.1",
    author = "Dror Atariah",
    author_email = "drorata@gmail.com",
    description = ("Scorer class that support multiple classes. Forked from https://github.com/StKyr/multiscorer"),
    license = "GNU General Public License v3.0",
    url = "https://github.com/drorata/multiscorer",
    packages=['multiscorer'],
    long_description=read('README.md'),
)
