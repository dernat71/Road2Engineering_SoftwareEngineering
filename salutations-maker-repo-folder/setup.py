from setuptools import setup
from pkg_resources import parse_requirements

with open("README.md", "r") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = []
    for req in parse_requirements(f.read()):
        requirements.append(str(req).replace('==', '>='))

setup(
    name="salutations-maker", # Replace with your own username
    version="0.0.1",
    author="Nathan Derave",
    author_email="nathan.derave@accenture.com",
    description="A package to say hello",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_dir={'': 'src'},
    install_requires=requirements,
    extras_require={
        'dev': ['pytest', 'flake8', 'tox'],
    }
    
)