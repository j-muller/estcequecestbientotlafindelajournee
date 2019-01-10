from os.path import join, dirname

from setuptools import setup, find_packages


def read(filename):
    with open(join(dirname(__file__), filename)) as fileobj:
        return fileobj.read()


def get_version(package):
    return [
        line for line in read('{}/version.py'.format(package)).splitlines()
        if line.startswith('__version__ = ')][0].split("'")[1]


PROJECT_NAME = 'estcequecestbientotlafindelajournee'
VERSION = get_version('estcequecestbientotlafindelajournee')


setup(
    name=PROJECT_NAME,
    version=VERSION,
    description="Est-ce que c'est bientot la fin de la journee ? webapp",
    author='Jeffrey Muller',
    author_email='jeffrey.muller92@gmail.com',
    url='https://github.com/j-muller/estcequecestbientotlafindelajournee',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'flask==1.0.2',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.5',
    ],
    package_data={'estcequecestbientotlafindelajournee': ['templates/*.html']},
    include_package_data=True,
)
