from setuptools import find_packages, setup
from shg.version import __version__, licence
from shg import __doc__, __author__, __author_email__

setup(
    name="tangods-shg",
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    license=licence,
    description="Tango Device Server for the shuntgroups based on the fasadedevice library",
    long_description=__doc__,
    url="https://github.com/synchrotron-solaris/dev-solaris-shg_ds.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["setuptools", "facadedevice", "pytango"],
    entry_points={
        "console_scripts": ["SHG = "
                            "shg.shg_ds.shg.SHG:run",
                            "RingSHG = "
                            "shg.ring_shg_ds.ring_shg.RingSHG:run",
                            "LandauSHG = "
                            "shg.landau_shg_ds.landau_shg.LandauSHG:run"]}
)
