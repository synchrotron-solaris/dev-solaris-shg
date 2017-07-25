from facadedevice import Facade, proxy_attribute, proxy_command
from tango import AttrWriteType, DevState


class LandauSHG(Facade):

    def safe_init_device(self):
        super(LandauSHG, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running")

    # Proxy attributes

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

    Pressure = proxy_attribute(
        dtype=float,
        property_name="PressureSource",
        access=AttrWriteType.READ
    )

    LowPressureAlarm = proxy_attribute(
        dtype=float,
        property_name="LowPressureAlarmSource",
        access=AttrWriteType.READ
    )

    CoolingCentralRod1Alarm = proxy_attribute(
        dtype=float,
        property_name="CoolingCentralRod1AlarmSource",
        access=AttrWriteType.READ
    )

    CoolingCentralRod2Alarm = proxy_attribute(
        dtype=float,
        property_name="CoolingCentralRod2AlarmSource",
        access=AttrWriteType.READ
    )

    CoolingMantelAlarm = proxy_attribute(
        dtype=float,
        property_name="CoolingMantelAlarmSource",
        access=AttrWriteType.READ
    )

    PIDSetpoint = proxy_attribute(
        dtype=float,
        property_name="PIDSetpointSource",
        access=AttrWriteType.READ
    )

    SelectSensorsType = proxy_attribute(
        dtype=float,
        property_name="SelectSensorsTypeSource",
        access=AttrWriteType.READ
    )

    SelectReturnSensorsNumber = proxy_attribute(
        dtype=float,
        property_name="SelectReturnSensorsNumberSource",
        access=AttrWriteType.READ
    )

    TempTwoReturnSensorsMean = proxy_attribute(
        dtype=float,
        property_name="TempTwoReturnSensorsMeanSource",
        access=AttrWriteType.READ
    )

    TempFourReturnSensorsMean = proxy_attribute(
        dtype=float,
        property_name="TempFourReturnSensorsMeanSource",
        access=AttrWriteType.READ
    )

    TempSupplyPipeSensor = proxy_attribute(
        dtype=float,
        property_name="TempSupplyPipeSensorSource",
        access=AttrWriteType.READ
    )

    TempReturnPipeSensor = proxy_attribute(
        dtype=float,
        property_name="TempReturnPipeSensorSource",
        access=AttrWriteType.READ
    )

    TempSurfaceSensorsMax = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensorsMaxSource",
        access=AttrWriteType.READ
    )

    TempSurfaceSensorsMin = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensorsMinSource",
        access=AttrWriteType.READ
    )

    TempSurfaceSensorsMean = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensorsMeanSource",
        access=AttrWriteType.READ
    )

    TempSurfaceSensor1= proxy_attribute(
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

    TempSupplySensor1 = proxy_attribute(
        dtype=float,
        property_name="TempSupplySensor1Source",
        access=AttrWriteType.READ
    )

    TempSupplySensor2 = proxy_attribute(
        dtype=float,
        property_name="TempSupplySensor2Source",
        access=AttrWriteType.READ
    )

    TempReturnSensor1 = proxy_attribute(
        dtype=float,
        property_name="TempReturnSensor1Source",
        access=AttrWriteType.READ
    )

    TempReturnSensor2 = proxy_attribute(
        dtype=float,
        property_name="TempReturnSensor2Source",
        access=AttrWriteType.READ
    )

    TempSensorBeforeEV = proxy_attribute(
        dtype=float,
        property_name="TempSensorBeforeEVSource",
        access=AttrWriteType.READ
    )

    TempSensorAfterEV = proxy_attribute(
        dtype=float,
        property_name="TempSensorAfterEVSource",
        access=AttrWriteType.READ
    )

    AtLeastTwoFaultySensors = proxy_attribute(
        dtype=float,
        property_name="AtLeastTwoFaultySensorsSource",
        access=AttrWriteType.READ
    )

    MainSetpoint = proxy_attribute(
        dtype=float,
        property_name="MainSetpointSource",
        access=AttrWriteType.READ_WRITE
    )

    SensorControl = proxy_attribute(
        dtype=float,
        property_name="SensorControlSource",
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

    SetpointAfterValve = proxy_attribute(
        dtype=float,
        property_name="SetpointAfterValveSource",
        access=AttrWriteType.READ_WRITE
    )

    SetpointAfterHeater = proxy_attribute(
        dtype=float,
        property_name="SetpointAfterHeaterSource",
        access=AttrWriteType.READ_WRITE
    )

    ChangeSetpoint = proxy_attribute(
        dtype=float,
        property_name="ChangeSetpointSource",
        access=AttrWriteType.READ_WRITE
    )

    ValveValue = proxy_attribute(
        dtype=float,
        property_name="ValveValueSource",
        access=AttrWriteType.READ
    )

    HeaterValue = proxy_attribute(
        dtype=float,
        property_name="HeaterValueSource",
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

    PlungerTempSensor = proxy_attribute(
        dtype=float,
        property_name="PlungerTempSensorSource",
        access=AttrWriteType.READ
    )

    StartPumpAttribute = proxy_attribute(
        dtype=bool,
        property_name="StartPumpSource",
        access=AttrWriteType.READ
    )

    StopPumpAttribute = proxy_attribute(
        dtype=bool,
        property_name="StopPumpSource",
        access=AttrWriteType.READ
    )

    ResetAttribute = proxy_attribute(
        dtype=bool,
        property_name="ResetSource",
        access=AttrWriteType.READ
    )

    # Proxy commands

    @proxy_command(
        property_name="StartPumpSource",
        write_attribute=True)
    def StartPump(self, subcommand):
        subcommand(1)

    @proxy_command(
        property_name="StopPumpSource",
        write_attribute=True)
    def StopPump(self, subcommand):
        subcommand(1)

    @proxy_command(
        property_name="ResetSource",
        write_attribute=True)
    def Reset(self, subcommand):
        subcommand(1)


run=LandauSHG.run_server()

if __name__ == '__main__':
   run()