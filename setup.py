import os
from setuptools import setup
from setuptools import find_packages

from emencia.django import socialaggregator


setup(name='emencia.django.socialaggregator',
      version=socialaggregator.__version__,
      description='A Django app for aggregate some feeds from social networks.',
      long_description=open('README.rst').read() + '\n' +
                       open(os.path.join('docs', 'HISTORY.txt')).read(),
      keywords='django, emencia, social networks, aggregation',
      classifiers=[
          'Framework :: Django',
          'Programming Language :: Python',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Development Status :: 2 - Pre-Alpha',
          'Topic :: Software Development :: Libraries :: Python Modules',],

      author=socialaggregator.__author__,
      author_email=socialaggregator.__email__,
      url=socialaggregator.__url__,

      license=socialaggregator.__license__,
      packages=find_packages(exclude=['demo']),
      namespace_packages=['emencia', 'emencia.django'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'django-taggit',
                        'django'])


