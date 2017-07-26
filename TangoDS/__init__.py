"""
DEV SHG SOLARIS
===============

This whole package contains three Device Classes for the shuntgroups. Those are:
* SHG
* RingSHG
* LandauSHG
"""

from setuptools import find_packages

__all__ = ['SHG', 'RingSHG', 'LandauSHG', 'version']
__doc__ = ""
__author__ = ""
__author_email__ = ""

for package_name in find_packages():
    package_import = __import__(package_name)
    __doc__ += "%s: %s" % (package_name, package_import.__doc__)
    __author__ += package_import.__author__ + ", "
    __author_email__ += package_import.__author_email__ + ", "
