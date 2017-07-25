|pic1|    |pic2|

.. |pic1| image:: _static/logo_solaris.bmp
   :width: 15%

.. |pic2| image:: _static/TANGO_controls_logo.png
   :width: 15%

LandauSHG Class
===============

**This class consists of the following parts:**

.. contents:: Table of contents

.. note::
   If not otherwise stated, all below are *float* and *READ*


Properties:
-----------
 - FlowFGE1Source
 - FlowFGE2Source
 - PressureSource
 - LowPressureAlarmSource
 - CoolingCentralRod1AlarmSource
 - CoolingCentralRod2AlarmSource
 - CoolingMantelAlarmSource
 - PIDSetpointSource
 - SelectSensorsTypeSource
 - SelectReturnSensorsNumberSource
 - TempTwoReturnSensorsMeanSource
 - TempFourReturnSensorsMeanSource
 - TempSupplyPipeSensorSource
 - TempReturnPipeSensorSource
 - TempSurfaceSensorsMaxSource
 - TempSurfaceSensorsMinSource
 - TempSurfaceSensorsMeanSource
 - TempSurfaceSensor1Source
 - TempSurfaceSensor2Source
 - TempSurfaceSensor3Source
 - TempSupplySensor1Source
 - TempSupplySensor2Source
 - TempReturnSensor1Source
 - TempReturnSensor2Source
 - TempSensorBeforeEVSource
 - TempSensorAfterEVSource
 - AtLeastTwoFaultySensorsSource
 - MainSetpointSource
 - SensorControlSource
 - ValveControlSource
 - EVControlSource
 - SetpointAfterValveSource
 - SetpointAfterHeaterSource
 - ChangeSetpointSource
 - ValveValueSource
 - HeaterValueSource
 - ValveControlErrorAlarmSource
 - HeaterControlErrorAlarmSource
 - PlungerTempSensorSource
 - StartPumpSource
 - StopPumpSource
 - ResetSource

Attributes:
-----------
 - FlowFGE1
 - FlowFGE2
 - Pressure
 - LowPressureAlarm
 - CoolingCentralRod1Alarm
 - CoolingCentralRod2Alarm
 - CoolingMantelAlarm
 - PIDSetpoint
 - SelectSensorsType
 - SelectReturnSensorsNumber
 - TempTwoReturnSensorsMean
 - TempFourReturnSensorsMean
 - TempSupplyPipeSensor
 - TempReturnPipeSensor
 - TempSurfaceSensorsMax
 - TempSurfaceSensorsMin
 - TempSurfaceSensorsMean
 - TempSurfaceSensor1
 - TempSurfaceSensor2
 - TempSurfaceSensor3
 - TempSupplySensor1
 - TempSupplySensor2
 - TempReturnSensor1
 - TempReturnSensor2
 - TempSensorBeforeEV
 - TempSensorAfterEV
 - AtLeastTwoFaultySensors
 - MainSetpoint (READ_WRITE)
 - SensorControl
 - ValveControl
 - EVControl
 - SetpointAfterValve (READ_WRITE)
 - SetpointAfterHeater (READ_WRITE)
 - ChangeSetpoint (READ_WRITE)
 - ValveValue
 - HeaterValue
 - ValveControlErrorAlarm
 - HeaterControlErrorAlarm
 - PlungerTempSensor
 - StartPumpAttribute, bool
 - StopPumpAttribute, bool
 - ResetAttribute, bool

Commands:
---------
 - StartPump: writes True to StartPumpSource
 - StopPump: writes True to StopPumpSource
 - Reset: writes True to ResetSource