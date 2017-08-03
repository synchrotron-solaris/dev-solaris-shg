"""
This is RingSHG device class based on the facadedevice
"""

from facadedevice import Facade, proxy_attribute, proxy_command
from tango import AttrWriteType, DevState


class RingSHG(Facade):

    def safe_init_device(self):
        """
        Docstring for 'safe_init_device' - it is just safe initialization of the DS
        :return:
        """
        super(RingSHG, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running")

    # Proxy attributes

    PressurePump1Alarm = proxy_attribute(
        dtype=float,
        property_name="PressurePump1AlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates Pump1 pressure alarm"
    )

    PressurePump2Alarm = proxy_attribute(
        dtype=float,
        property_name="PressurePump2AlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates Pump2 pressure alarm"
    )

    FlowFGE1 = proxy_attribute(
        dtype=float,
        property_name="FlowFGE1Source",
        access=AttrWriteType.READ,
        description="This attribute specifies flowFGE1"
    )

    FlowFGE2 = proxy_attribute(
        dtype=float,
        property_name="FlowFGE2Source",
        access=AttrWriteType.READ,
        description="This attribute specifies flowFGE2"
    )

    PressureRead = proxy_attribute(
        dtype=float,
        property_name="PressureReadSource",
        access=AttrWriteType.READ,
        description="This attribute specifies pressure (read)"
    )

    FlowCirculator = proxy_attribute(
        dtype=float,
        property_name="FlowCirculatorSource",
        access=AttrWriteType.READ,
        description="This attribute specifies flow circulator"
    )

    InnerConductorAlarm = proxy_attribute(
        dtype=float,
        property_name="InnerConductorAlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates inner conductor alarm"
    )

    OuterConductorAlarm = proxy_attribute(
        dtype=float,
        property_name="OuterConductorAlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates outer conductor alarm"
    )

    MantelAlarm1 = proxy_attribute(
        dtype=float,
        property_name="MantelAlarm1Source",
        access=AttrWriteType.READ,
        description="This attribute indicates mantel alarm1"
    )

    MantelAlarm2 = proxy_attribute(
        dtype=float,
        property_name="MantelAlarm2Source",
        access=AttrWriteType.READ,
        description="This attribute indicates mantel alarm2"
    )

    MantelAlarm3 = proxy_attribute(
        dtype=float,
        property_name="MantelAlarm3Source",
        access=AttrWriteType.READ,
        description="This attribute indicates mantel alarm3"
    )

    TuningEndcapAlarm = proxy_attribute(
        dtype=float,
        property_name="TuningEndcapAlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates tuning endcap alarm"
    )

    StaticEndcapAlarm = proxy_attribute(
        dtype=float,
        property_name="StaticEndcapAlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates static endcap alarm"
    )

    InnerRodAlarm1 = proxy_attribute(
        dtype=float,
        property_name="InnerRodAlarm1Source",
        access=AttrWriteType.READ,
        description="This attribute indicates inner rod alarm1"
    )

    InnerRodAlarm2 = proxy_attribute(
        dtype=float,
        property_name="InnerRodAlarm2Source",
        access=AttrWriteType.READ,
        description="This attribute indicates inner rod alarm2"
    )

    SHGAlarm = proxy_attribute(
        dtype=float,
        property_name="SHGAlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates shg_ds alarm"
    )

    CirculatorDummyLoadAlarm = proxy_attribute(
        dtype=float,
        property_name="CirculatorDummyLoadAlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates circulator dummy load alarm"
    )

    TransmitterAlarm1 = proxy_attribute(
        dtype=float,
        property_name="TransmitterAlarm1Source",
        access=AttrWriteType.READ,
        description="This attribute indicates transmitter alarm1"
    )

    TransmitterAlarm2 = proxy_attribute(
        dtype=float,
        property_name="TransmitterAlarm2Source",
        access=AttrWriteType.READ,
        description="This attribute indicates transmitter alarm2"
    )

    MobileDummyLoadAlarm = proxy_attribute(
        dtype=float,
        property_name="MobileDummyLoadAlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates mobile dummy load alarm"
    )

    RF1CirculatorAlarm = proxy_attribute(
        dtype=float,
        property_name="RF1CirculatorAlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates RF1 circulator alarm"
    )

    PIDSetpoint = proxy_attribute(
        dtype=float,
        property_name="PIDSetpointSource",
        access=AttrWriteType.READ,
        description="This attribute specifies PID setpoint"
    )

    TempBeforePump = proxy_attribute(
        dtype=float,
        property_name="TempBeforePumpSource",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature before pump"
    )

    TempReturn = proxy_attribute(
        dtype=float,
        property_name="TempReturnSource",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature return"
    )

    SelectedSensors = proxy_attribute(
        dtype=float,
        property_name="SelectedSensorsSource",
        access=AttrWriteType.READ,
        description="This attribute specifies selected sensors"
    )

    TempSurfaceSensors = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensorsSource",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature surface sensors"
    )

    TempImmerseSensors = proxy_attribute(
        dtype=float,
        property_name="TempImmerseSensorsSource",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature immerse sensors"
    )

    MainSetpoint = proxy_attribute(
        dtype=float,
        property_name="MainSetpointSource",
        access=AttrWriteType.READ_WRITE,
        description="This attribute specifies main setpoint"
    )

    TempAfterPump = proxy_attribute(
        dtype=float,
        property_name="TempAfterPumpSource",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature after pump"
    )

    TempAfterHeater = proxy_attribute(
        dtype=float,
        property_name="TempAfterHeaterSource",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature after heater"
    )

    SetpointAfterValve = proxy_attribute(
        dtype=float,
        property_name="SetpointAfterValveSource",
        access=AttrWriteType.READ,
        description="This attribute specifies setpoint after valve"
    )

    SetpointAfterHeater = proxy_attribute(
        dtype=float,
        property_name="SetpointAfterHeaterSource",
        access=AttrWriteType.READ,
        description="This attribute specifies setpoint after heater"
    )

    ChangeHeaterSetpoint = proxy_attribute(
        dtype=float,
        property_name="ChangeHeaterSetpointSource",
        access=AttrWriteType.READ_WRITE,
        description="This attribute specifies heater setpoint change"
    )

    TempSurfaceSensor1 = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor1Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature on surface sensor1"
    )

    TempSurfaceSensor2 = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor2Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature on surface sensor2"
    )

    TempSurfaceSensor3 = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor3Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature on surface sensor"
    )

    TempSurfaceSensor4 = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor4Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature on surface sensor4"
    )

    TempSurfaceSensor5 = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor5Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature on surface sensor5"
    )

    TempSurfaceSensor6 = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor6Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature on surface sensor6"
    )

    TempImmerseSensor1 = proxy_attribute(
        dtype=float,
        property_name="TempImmerseSensor1Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature on immerse sensor1"
    )

    TempImmerseSensor2 = proxy_attribute(
        dtype=float,
        property_name="TempImmerseSensor2Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature on immerse sensor2"
    )

    CavityControlErrorAlarm = proxy_attribute(
        dtype=float,
        property_name="CavityControlErrorAlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates cavity control error alarm"
    )

    ValveControlErrorAlarm = proxy_attribute(
        dtype=float,
        property_name="ValveControlErrorAlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates valve control error alarm"
    )

    HeaterControlErrorAlarm = proxy_attribute(
        dtype=float,
        property_name="HeaterControlErrorAlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates heater control error alarm"
    )

    ROLowLimit = proxy_attribute(
        dtype=float,
        property_name="ROLowLimitSource",
        access=AttrWriteType.READ,
        description="This attribute indicates RO low limit"
    )

    ROHighLimit = proxy_attribute(
        dtype=float,
        property_name="ROHighLimitSource",
        access=AttrWriteType.READ,
        description="This attribute indicates RO high limit"
    )

    ImmerseSensorsDefective = proxy_attribute(
        dtype=float,
        property_name="ImmerseSensorsDefectiveSource",
        access=AttrWriteType.READ,
        description="This attribute indicates immerse sensors defect"
    )

    ImmerseSensorDefective = proxy_attribute(
        dtype=float,
        property_name="ImmerseSensorDefectiveSource",
        access=AttrWriteType.READ,
        description="This attribute indicates immerse sensor defect"
    )

    SurfaceSensorsDefective = proxy_attribute(
        dtype=float,
        property_name="SurfaceSensorsDefectiveSource",
        access=AttrWriteType.READ,
        description="This attribute indicates surface sensors defect"
    )

    SurfaceSensorDefective = proxy_attribute(
        dtype=float,
        property_name="SurfaceSensorDefectiveSource",
        access=AttrWriteType.READ,
        description="This attribute indicates surface sensor defect"
    )

    SensorsControl = proxy_attribute(
        dtype=float,
        property_name="SensorsControlSource",
        access=AttrWriteType.READ,
        description="This attribute specifies sensors control"
    )

    ValveControl = proxy_attribute(
        dtype=float,
        property_name="ValveControlSource",
        access=AttrWriteType.READ,
        description="This attribute specifies valve control"
    )

    EVControl = proxy_attribute(
        dtype=float,
        property_name="EVControlSource",
        access=AttrWriteType.READ,
        description="This attribute specifies EV control"
    )

    ValveControlValue = proxy_attribute(
        dtype=float,
        property_name="ValveControlValueSource",
        access=AttrWriteType.READ,
        description="This attribute specifies valve control value"
    )

    HeaterControlValue = proxy_attribute(
        dtype=float,
        property_name="HeaterControlValueSource",
        access=AttrWriteType.READ,
        description="This attribute specifies heater control value"
    )

    ResetAttribute = proxy_attribute(
        dtype=bool,
        property_name="ResetSource",
        access=AttrWriteType.READ_WRITE,
        description="This attribute resets pumps"
    )

    StopPumpsAttribute = proxy_attribute(
        dtype=bool,
        property_name="StopPumpsSource",
        access=AttrWriteType.READ_WRITE,
        description="This attribute stops pumps"
    )

    StartPump1Attribute = proxy_attribute(
        dtype=bool,
        property_name="StartPump1Source",
        access=AttrWriteType.READ_WRITE,
        description="This attribute starts pump1"
    )

    StartPump2Attribute = proxy_attribute(
        dtype=bool,
        property_name="StartPump2Source",
        access=AttrWriteType.READ_WRITE,
        description="This attribute starts pump2"
    )

    SwitchPumpsAttribute = proxy_attribute(
        dtype=bool,
        property_name="SwitchPumpsSource",
        access=AttrWriteType.READ_WRITE,
        description="This attribute switches pumps"
    )



    # Proxy commands

    @proxy_command(
        property_name="ResetSource",
        write_attribute=True)
    def Reset(self, subcommand):
        """
        This command resets pumps
        :param subcommand:
        :return:
        """
        subcommand(1)

    @proxy_command(
        property_name="StopPumpsSource",
        write_attribute=True)
    def StopPumps(self, subcommand):
        """
        This command stops pumps.
        :param subcommand:
        :return:
        """
        subcommand(1)

    @proxy_command(
        property_name="StartPump1Source",
        write_attribute=True)
    def StartPump1(self, subcommand):
        """
        This command starts pump1
        :param subcommand:
        :return:
        """
        subcommand(1)

    @proxy_command(
        property_name="StartPump2Source",
        write_attribute=True)
    def StartPump2(self, subcommand):
        """
        This command starts pump2.
        :param subcommand:
        :return:
        """
        subcommand(1)

    @proxy_command(
        property_name="SwitchPumpsSource",
        write_attribute=True)
    def SwitchPumps(self, subcommand):
        """
        This command switches pumps.
        :param subcommand:
        :return:
        """
        subcommand(1)

if __name__ == '__main__':
   RingSHG.run_server()
