#!/usr/bin/env python
from setuptools import setup
import subprocess

try:
    subprocess.call(['conda','install','--file','requirements.txt'])
except Exception as e:
    pass


setup(name='nmeautils',
	  description='read NMEA with Python',
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/nmeautils',
      install_requires=['pathlib2'],
      packages=['nmeautils'],
	  )

