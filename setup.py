from setuptools import find_packages, setup
from SHG.version import __version__, licence
from SHG import __doc__, __author__, __author_email__

setup(
    name="SHG TangoDS",
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
                            "SHG.SHG.SHG:run"
                            "RingSHG = "
                            "SHG.RingSHG.RingSHG:run"
                            "LandauSHG = "
                            "SHG.LandauSHG.LandauSHG:run"]}
)