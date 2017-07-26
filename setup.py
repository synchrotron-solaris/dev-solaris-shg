from setuptools import find_packages, setup
from TangoDS.version import __version__, licence
from TangoDS import __doc__, __author__, __author_email__

setup(
    name="SHG_DS TangoDS",
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    license=licence,
    description="Tango Device Server for the shuntgroups based on the fasadedevice library",
    long_description=__doc__,
    url="https://github.com/synchrotron-solaris/dev-solaris-shg.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["setuptools", "facadedevice", "pytango"],
    entry_points={
        "console_scripts": ["SHG = "
                            "TangoDS.SHG_DS.SHG.shg:run",
                            "RingSHG = "
                            "TangoDS.RingSHG_DS.RingSHG.ringshg:run",
                            "LandauSHG = "
                            "TangoDS.LandauSHG_DS.LandauSHG.landaushg:run"]}
)
