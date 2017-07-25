DEV-SOLARIS-SHG
===============

Tango Device Server for the shuntgroups based on the fasadedevice library. Each is launched on
its own Device Class.

This is a sample Python project that follows
[NSRC SOLARIS coding policies](http://gitlab.m.cps.uj.edu.pl/CSIT/doc-solaris-coding-policies).


What's inside
-------------
There are directories for source code, documentation as well as
`LICENCE` file as well as a setup script.

How to install
--------------
Tested on CentOS7

Firstly, open TangoTest Container as a root:
```console
docker exec -it -u 0 tangotestcontainername bash
```
Then install GIT:
```console
yum install git
```
Clone repository end enter to it:
```console
git clone URL
cd NAME
```
Finally, you can use:
```console
python setup.py install
```
or:
```console
pip install .
```
Now simply type:
```console
DS_NAME DS_INSTANCE
```
**WARNING**: both DS_NAME and DS_INSTANCE must be already declared in database

Requirements
------------
Requirements for this project are:
 - `setuptools`
 - `facadedevice`
 - `tango`

License
-------
This sample project is distributed under LGPLv3 (see `LICENSE` file).
