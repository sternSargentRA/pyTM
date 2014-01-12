from distutils.core import setup
import os


def is_package(path):
    return (
        os.path.isdir(path) and
        os.path.isfile(os.path.join(path, '__init__.py'))
        )


def find_packages(path, base=""):
    """ Find all packages in path """
    packages = {}
    for item in os.listdir(path):
        dir = os.path.join(path, item)
        if is_package(dir):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item
            packages[module_name] = dir
            packages.update(find_packages(dir, module_name))
    return packages

setup(
    name='pyTM',
    version='0.0.1',
    author='Chase Coleman, Spencer Lyon, and Thomas Sargent',
    author_email='sgl290@stern.nyu.edu',
    packages=find_packages('.'),
    url='https://github.com/spencerlyon2/pyTM',
    description='pyTM is awesome',
    long_description=open('README.rst').read()
)
