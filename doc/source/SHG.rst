|pic1|    |pic2|

.. |pic1| image:: _static/logo_solaris.bmp
   :width: 15%

.. |pic2| image:: _static/TANGO_controls_logo.png
   :width: 15%

SHG Class
=========

**This class consists of the following parts:**

.. contents:: Table of contents

.. note::
   If not otherwise stated, all below are *float* and *READ*


Properties:
-----------
 - TemperatureModbus
 - TemperatureSetpointModbus
 - SledSetpointModbus
 - SledMasterModbus
 - SledSlaveModbus
 - SledHeaterOutModbus
 - Linac1SetpointModbus
 - Linac1MasterModbus
 - Linac1SlaveModbus
 - Linac1HeaterOutModbus
 - Linac2SetpointModbus
 - Linac2MasterModbus
 - Linac2SlaveModbus
 - Linac2HeaterOutModbus
 - WaterSetpointModbus
 - WaterInModbus
 - WaterOutModbus
 - WaterAfterPumpModbus
 - ValveModbus
 - Sled2Modbus
 - FlowTag
 - PressureTag
 - PressureSetpointTag
 - PressureAlarmTag
 - StartPumpTag
 - StopPumpTag
 - ResetTag

Attributes:
-----------
 - Temperature
 - TemperatureSetpoint (READ_WRITE)
 - SledSetpoint (READ_WRITE)
 - SledMaster
 - SledSlave
 - SledHeaterOut
 - Linac1Setpoint (READ_WRITE)
 - Linac1Master
 - Linac1Slave
 - Linac1HeaterOut
 - Linac2Setpoint (READ_WRITE)
 - Linac2Master
 - Linac2Slave
 - Linac2HeaterOut
 - WaterSetpoint (READ_WRITE)
 - WaterIn
 - WaterOut
 - WaterAfterPump
 - Valve
 - Sled2
 - Flow
 - Pressure
 - PressureSetpoint (READ_WRITE)
 - PressureAlarm
 - StartPump (READ_WRITE), bool
 - StopPump (READ_WRITE), bool
 - Reset (READ_WRITE), bool

Commands:
---------
 - StartPump: writes True to StartPumpTag
 - StopPump: writes True to StopPumpTag
 - Reset: writes True to ResetTag