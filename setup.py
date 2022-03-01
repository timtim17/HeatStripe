"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['HeatStripe.py']
DATA_FILES = ['g19.png']
OPTIONS = {'iconfile': '/Users/aus/Desktop/HeatStripe/g19.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)