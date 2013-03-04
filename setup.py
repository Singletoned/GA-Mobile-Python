#!/usr/bin/env python

from distutils.core import setup

requires = """
requests
"""

setup(name='mobile_google_analytics',
      version='1.0',
      description='Google Analytics Python Module',
      author='b1tr0t',
      author_email='',
      url='https://github.com/b1tr0t/Google-Analytics-for-Mobile--python-',
      packages=['ga_app',],
      py_modules=['ga',],
      install_requires=requires)
