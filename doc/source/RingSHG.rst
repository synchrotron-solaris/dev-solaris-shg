|pic1|    |pic2|

.. |pic1| image:: _static/logo_solaris.bmp
   :width: 15%

.. |pic2| image:: _static/TANGO_controls_logo.png
   :width: 15%

RingSHG Class
=============

**This class consists of the following parts:**

.. contents:: Table of contents

.. note::
   If not otherwise stated, all below are *float* and *READ*


Properties:
-----------
 - PressurePump1AlarmSource
 - PressurePump2AlarmSource
 - FlowFGE1Source
 - FlowFGE2Source
 - PressureReadSource
 - FlowCirculatorSource
 - InnerConductorAlarmSource
 - OuterConductorAlarmSource
 - MantelAlarm1Source
 - MantelAlarm2Source
 - MantelAlarm3Source
 - TuningEndcapAlarmSource
 - StaticEndcapAlarmSource
 - InnerRodAlarm1Source
 - InnerRodAlarm2Source
 - SHGAlarmSource
 - CirculatorDummyLoadAlarmSource
 - TransmitterAlarm1Source
 - TransmitterAlarm2Source
 - MobileDummyLoadAlarmSource
 - RF1CirculatorAlarmSource
 - PIDSetpointSource
 - TempBeforePumpSource
 - TempReturnSource
 - SelectedSensorsSource
 - TempSurfaceSensorsSource
 - TempImmerseSensorsSource
 - MainSetpointSource
 - TempAfterPumpSource
 - TempAfterHeaterSource
 - SetpointAfterValveSource
 - SetpointAfterHeaterSource
 - ChangeHeaterSetpointSource
 - TempSurfaceSensor1Source
 - TempSurfaceSensor2Source
 - TempSurfaceSensor3Source
 - TempSurfaceSensor4Source
 - TempSurfaceSensor5Source
 - TempSurfaceSensor6Source
 - TempImmerseSensor1Source
 - TempImmerseSensor2Source
 - CavityControlErrorAlarmSource
 - ValveControlErrorAlarmSource
 - HeaterControlErrorAlarmSource
 - ROLowLimitSource
 - ROHighLimitSource
 - ImmerseSensorsDefectiveSource
 - ImmerseSensorDefectiveSource
 - SurfaceSensorsDefectiveSource
 - SurfaceSensorDefectiveSource
 - SensorsControlSource
 - ValveControlSource
 - EVControlSource
 - ValveControlValueSource
 - HeaterControlValueSource
 - ResetSource
 - StopPumpsSource
 - StartPump1Source
 - StartPump2Source
 - SwitchPumpsSource

Attributes:
-----------
 - PressurePump1Alarm
 - PressurePump2Alarm
 - FlowFGE1
 - FlowFGE2
 - PressureRead
 - FlowCirculator
 - InnerConductorAlarm
 - OuterConductorAlarm
 - MantelAlarm1
 - MantelAlarm2
 - MantelAlarm3
 - TuningEndcapAlarm
 - StaticEndcapAlarm
 - InnerRodAlarm1
 - InnerRodAlarm2
 - SHGAlarm
 - CirculatorDummyLoadAlarm
 - TransmitterAlarm1
 - TransmitterAlarm2
 - MobileDummyLoadAlarm
 - RF1CirculatorAlarm
 - PIDSetpoint
 - TempBeforePump
 - TempReturn
 - SelectedSensors
 - TempSurfaceSensors
 - TempImmerseSensors
 - MainSetpoint (READ_WRITE)
 - TempAfterPump
 - TempAfterHeater
 - SetpointAfterValve
 - SetpointAfterHeater
 - ChangeHeaterSetpoint (READ_WRITE)
 - TempSurfaceSensor1
 - TempSurfaceSensor2
 - TempSurfaceSensor3
 - TempSurfaceSensor4
 - TempSurfaceSensor5
 - TempSurfaceSensor6
 - TempImmerseSensor1
 - TempImmerseSensor2
 - CavityControlErrorAlarm
 - ValveControlErrorAlarm
 - HeaterControlErrorAlarm
 - ROLowLimit
 - ROHighLimit
 - ImmerseSensorsDefective
 - ImmerseSensorDefective
 - SurfaceSensorsDefective
 - SurfaceSensorDefective
 - SensorsControl
 - ValveControl
 - EVControl
 - ValveControlValue
 - HeaterControlValue
 - ResetAttribute (READ_WRITE, bool
 - StopPumpsAttribute (READ_WRITE), bool
 - StartPump1Attribute (READ_WRITE), bool
 - StartPump2Attribute (READ_WRITE), bool
 - SwitchPumpsAttribute (READ_WRITE), bool

Commands:
---------
 - Reset: writes True to ResetSource
 - StopPumps: writes True to StopPumpsSource
 - StartPump1: writes True to StartPump1Source
 - StartPump2: writes True to StartPump2Source
 - SwitchPumps: writes True to SwitchPumpsSource