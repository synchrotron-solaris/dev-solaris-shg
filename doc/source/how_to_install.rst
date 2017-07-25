|pic1|    |pic2|

.. |pic1| image:: _static/logo_solaris.bmp
   :width: 15%

.. |pic2| image:: _static/TANGO_controls_logo.png
   :width: 15%

How to install
==============

.. note:: **TESTED ON CENTOS7**

Firstly, open TangoTest Container as a root::

   docker exec -it -u 0 tangotestcontainername bash

Then install GIT::

   yum install git

Clone repository end enter to it::

   git clone URL
   cd NAME

Finally, you can use::

   python setup.py install

or::

   pip install .

Now simply type::

   DS_NAME DS_INSTANCE

.. important:: Both DS_NAME and DS_INSTANCE must be already declared in database


