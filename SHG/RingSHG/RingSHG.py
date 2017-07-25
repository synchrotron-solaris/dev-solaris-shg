from facadedevice import Facade, proxy_attribute, proxy_command
from tango import AttrWriteType, DevState


class RingSHG(Facade):

    def safe_init_device(self):
        super(RingSHG, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running")

    # Proxy attributes

    PressurePump1Alarm = proxy_attribute(
        dtype=float,
        property_name="PressurePump1AlarmSource",
        access=AttrWriteType.READ
    )

    PressurePump2Alarm = proxy_attribute(
        dtype=float,
        property_name="PressurePump2AlarmSource",
        access=AttrWriteType.READ
    )

    FlowFGE1 = proxy_attribute(
        dtype=float,
        property_name="FlowFGE1Source",
        access=AttrWriteType.READ
    )

    FlowFGE2 = proxy_attribute(
        dtype=float,
        property_name="FlowFGE2Source",
        access=AttrWriteType.READ
    )

    PressureRead = proxy_attribute(
        dtype=float,
        property_name="PressureReadSource",
        access=AttrWriteType.READ
    )

    FlowCirculator = proxy_attribute(
        dtype=float,
        property_name="FlowCirculatorSource",
        access=AttrWriteType.READ
    )

    InnerConductorAlarm = proxy_attribute(
        dtype=float,
        property_name="InnerConductorAlarmSource",
        access=AttrWriteType.READ
    )

    OuterConductorAlarm = proxy_attribute(
        dtype=float,
        property_name="OuterConductorAlarmSource",
        access=AttrWriteType.READ
    )

    MantelAlarm1 = proxy_attribute(
        dtype=float,
        property_name="MantelAlarm1Source",
        access=AttrWriteType.READ
    )

    MantelAlarm2 = proxy_attribute(
        dtype=float,
        property_name="MantelAlarm2Source",
        access=AttrWriteType.READ
    )

    MantelAlarm3 = proxy_attribute(
        dtype=float,
        property_name="MantelAlarm3Source",
        access=AttrWriteType.READ
    )

    TuningEndcapAlarm = proxy_attribute(
        dtype=float,
        property_name="TuningEndcapAlarmSource",
        access=AttrWriteType.READ
    )

    StaticEndcapAlarm = proxy_attribute(
        dtype=float,
        property_name="StaticEndcapAlarmSource",
        access=AttrWriteType.READ
    )

    InnerRodAlarm1 = proxy_attribute(
        dtype=float,
        property_name="InnerRodAlarm1Source",
        access=AttrWriteType.READ
    )

    InnerRodAlarm2 = proxy_attribute(
        dtype=float,
        property_name="InnerRodAlarm2Source",
        access=AttrWriteType.READ
    )

    SHGAlarm = proxy_attribute(
        dtype=float,
        property_name="SHGAlarmSource",
        access=AttrWriteType.READ
    )

    CirculatorDummyLoadAlarm = proxy_attribute(
        dtype=float,
        property_name="CirculatorDummyLoadAlarmSource",
        access=AttrWriteType.READ
    )

    TransmitterAlarm1 = proxy_attribute(
        dtype=float,
        property_name="TransmitterAlarm1Source",
        access=AttrWriteType.READ
    )

    TransmitterAlarm2 = proxy_attribute(
        dtype=float,
        property_name="TransmitterAlarm2Source",
        access=AttrWriteType.READ
    )

    MobileDummyLoadAlarm = proxy_attribute(
        dtype=float,
        property_name="MobileDummyLoadAlarmSource",
        access=AttrWriteType.READ
    )

    RF1CirculatorAlarm = proxy_attribute(
        dtype=float,
        property_name="RF1CirculatorAlarmSource",
        access=AttrWriteType.READ
    )

    PIDSetpoint = proxy_attribute(
        dtype=float,
        property_name="PIDSetpointSource",
        access=AttrWriteType.READ
    )

    TempBeforePump = proxy_attribute(
        dtype=float,
        property_name="TempBeforePumpSource",
        access=AttrWriteType.READ
    )

    TempReturn = proxy_attribute(
        dtype=float,
        property_name="TempReturnSource",
        access=AttrWriteType.READ
    )

    SelectedSensors = proxy_attribute(
        dtype=float,
        property_name="SelectedSensorsSource",
        access=AttrWriteType.READ
    )

    TempSurfaceSensors = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensorsSource",
        access=AttrWriteType.READ
    )

    TempImmerseSensors = proxy_attribute(
        dtype=float,
        property_name="TempImmerseSensorsSource",
        access=AttrWriteType.READ
    )

    MainSetpoint = proxy_attribute(
        dtype=float,
        property_name="MainSetpointSource",
        access=AttrWriteType.READ_WRITE
    )

    TempAfterPump = proxy_attribute(
        dtype=float,
        property_name="TempAfterPumpSource",
        access=AttrWriteType.READ
    )

    TempAfterHeater = proxy_attribute(
        dtype=float,
        property_name="TempAfterHeaterSource",
        access=AttrWriteType.READ
    )

    SetpointAfterValve = proxy_attribute(
        dtype=float,
        property_name="SetpointAfterValveSource",
        access=AttrWriteType.READ
    )

    SetpointAfterHeater = proxy_attribute(
        dtype=float,
        property_name="SetpointAfterHeaterSource",
        access=AttrWriteType.READ
    )

    ChangeHeaterSetpoint = proxy_attribute(
        dtype=float,
        property_name="ChangeHeaterSetpointSource",
        access=AttrWriteType.READ_WRITE
    )

    TempSurfaceSensor1 = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor1Source",
        access=AttrWriteType.READ
    )

    TempSurfaceSensor2 = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor2Source",
        access=AttrWriteType.READ
    )

    TempSurfaceSensor3 = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor3Source",
        access=AttrWriteType.READ
    )

    TempSurfaceSensor4 = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor4Source",
        access=AttrWriteType.READ
    )

    TempSurfaceSensor5 = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor5Source",
        access=AttrWriteType.READ
    )

    TempSurfaceSensor6 = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor6Source",
        access=AttrWriteType.READ
    )

    TempImmerseSensor1 = proxy_attribute(
        dtype=float,
        property_name="TempImmerseSensor1Source",
        access=AttrWriteType.READ
    )

    TempImmerseSensor2 = proxy_attribute(
        dtype=float,
        property_name="TempImmerseSensor2Source",
        access=AttrWriteType.READ
    )

    CavityControlErrorAlarm = proxy_attribute(
        dtype=float,
        property_name="CavityControlErrorAlarmSource",
        access=AttrWriteType.READ
    )

    ValveControlErrorAlarm = proxy_attribute(
        dtype=float,
        property_name="ValveControlErrorAlarmSource",
        access=AttrWriteType.READ
    )

    HeaterControlErrorAlarm = proxy_attribute(
        dtype=float,
        property_name="HeaterControlErrorAlarmSource",
        access=AttrWriteType.READ
    )

    ROLowLimit = proxy_attribute(
        dtype=float,
        property_name="ROLowLimitSource",
        access=AttrWriteType.READ
    )

    ROHighLimit = proxy_attribute(
        dtype=float,
        property_name="ROHighLimitSource",
        access=AttrWriteType.READ
    )

    ImmerseSensorsDefective = proxy_attribute(
        dtype=float,
        property_name="ImmerseSensorsDefectiveSource",
        access=AttrWriteType.READ
    )

    ImmerseSensorDefective = proxy_attribute(
        dtype=float,
        property_name="ImmerseSensorDefectiveSource",
        access=AttrWriteType.READ
    )

    SurfaceSensorsDefective = proxy_attribute(
        dtype=float,
        property_name="SurfaceSensorsDefectiveSource",
        access=AttrWriteType.READ
    )

    SurfaceSensorDefective = proxy_attribute(
        dtype=float,
        property_name="SurfaceSensorDefectiveSource",
        access=AttrWriteType.READ
    )

    SensorsControl = proxy_attribute(
        dtype=float,
        property_name="SensorsControlSource",
        access=AttrWriteType.READ
    )

    ValveControl = proxy_attribute(
        dtype=float,
        property_name="ValveControlSource",
        access=AttrWriteType.READ
    )

    EVControl = proxy_attribute(
        dtype=float,
        property_name="EVControlSource",
        access=AttrWriteType.READ
    )

    ValveControlValue = proxy_attribute(
        dtype=float,
        property_name="ValveControlValueSource",
        access=AttrWriteType.READ
    )

    HeaterControlValue = proxy_attribute(
        dtype=float,
        property_name="HeaterControlValueSource",
        access=AttrWriteType.READ
    )

    ResetAttribute = proxy_attribute(
        dtype=bool,
        property_name="ResetSource",
        access=AttrWriteType.READ_WRITE
    )

    StopPumpsAttribute = proxy_attribute(
        dtype=bool,
        property_name="StopPumpsSource",
        access=AttrWriteType.READ_WRITE
    )

    StartPump1Attribute = proxy_attribute(
        dtype=bool,
        property_name="StartPump1Source",
        access=AttrWriteType.READ_WRITE
    )

    StartPump2Attribute = proxy_attribute(
        dtype=bool,
        property_name="StartPump2Source",
        access=AttrWriteType.READ_WRITE
    )

    SwitchPumpsAttribute = proxy_attribute(
        dtype=bool,
        property_name="SwitchPumpsSource",
        access=AttrWriteType.READ_WRITE
    )



    # Proxy commands

    @proxy_command(
        property_name="ResetSource",
        write_attribute=True)
    def Reset(self, subcommand):
        subcommand(1)

    @proxy_command(
        property_name="StopPumpsSource",
        write_attribute=True)
    def StopPumps(self, subcommand):
        subcommand(1)

    @proxy_command(
        property_name="StartPump1Source",
        write_attribute=True)
    def StartPump1(self, subcommand):
        subcommand(1)

    @proxy_command(
        property_name="StartPump2Source",
        write_attribute=True)
    def StartPump2(self, subcommand):
        subcommand(1)

    @proxy_command(
        property_name="SwitchPumpsSource",
        write_attribute=True)
    def SwitchPumps(self, subcommand):
        subcommand(1)


run=RingSHG.run_server()

if __name__ == '__main__':
   run()