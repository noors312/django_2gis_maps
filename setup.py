import os
from setuptools import setup

README = os.path.join(os.path.dirname(__file__), 'README.md')
LONG_DESCRIPTION = open(README, 'r').read()
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Framework :: Django",
    "Framework :: Django :: 1.11",
    "Framework :: Django :: 2.0",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "kajshdkajshdjasd"
]

setup(
    name="django_2gis_maps",
    version='1.0.3',
    author="Noors Ergesh",
    author_email="jackmovies01@gmail.com",
    description="Plugs 2gis maps for Django admin",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/NursErgesh/django_2gis_maps.git",
    packages=("django_2gis_maps",),
    include_package_data=True,
    install_requires=open('requirements/requirements.txt').read().splitlines(),
    tests_require=open('requirements/test.txt').read().splitlines(),
    classifiers=CLASSIFIERS,
    zip_safe=False,
)
