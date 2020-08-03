from setuptools import setup
from pkg_resources import parse_requirements

with open("README.md", "r") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = []
    for req in parse_requirements(f.read()):
        requirements.append(str(req).replace('==', '>='))

setup(
    long_description=long_description,
    install_requires=requirements)