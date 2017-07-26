"""
This is LandauSHG device class based on the facadedevice
"""

from facadedevice import Facade, proxy_attribute, proxy_command
from tango import AttrWriteType, DevState


class LandauSHG(Facade):

    def safe_init_device(self):
        """
        Docstring for 'safe_init_device' - it is just safe initialization of the DS
        :return:
        """
        super(LandauSHG, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running")

    # Proxy attributes

    FlowFGE1 = proxy_attribute(
        dtype=float,
        property_name="FlowFGE1Source",
        access=AttrWriteType.READ,
        description="This attribute specifies FlowFGE1"
    )

    FlowFGE2 = proxy_attribute(
        dtype=float,
        property_name="FlowFGE2Source",
        access=AttrWriteType.READ,
        description="This attribute specifies FlowFGE2"
    )

    Pressure = proxy_attribute(
        dtype=float,
        property_name="PressureSource",
        access=AttrWriteType.READ,
        description="This attribute specifies pressure"
    )

    LowPressureAlarm = proxy_attribute(
        dtype=float,
        property_name="LowPressureAlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates low pressure alarm"
    )

    CoolingCentralRod1Alarm = proxy_attribute(
        dtype=float,
        property_name="CoolingCentralRod1AlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates cooling central rod1 alarm"
    )

    CoolingCentralRod2Alarm = proxy_attribute(
        dtype=float,
        property_name="CoolingCentralRod2AlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates cooling central rod2 alarm"
    )

    CoolingMantelAlarm = proxy_attribute(
        dtype=float,
        property_name="CoolingMantelAlarmSource",
        access=AttrWriteType.READ,
        description="This attribute indicates cooling mantel alarm"
    )

    PIDSetpoint = proxy_attribute(
        dtype=float,
        property_name="PIDSetpointSource",
        access=AttrWriteType.READ,
        description="This attribute specifies PID setpoint"
    )

    SelectSensorsType = proxy_attribute(
        dtype=float,
        property_name="SelectSensorsTypeSource",
        access=AttrWriteType.READ,
        description="This attribute specifies sensor type selection"
    )

    SelectReturnSensorsNumber = proxy_attribute(
        dtype=float,
        property_name="SelectReturnSensorsNumberSource",
        access=AttrWriteType.READ,
        description="This attribute specifies select return sensors number"
    )

    TempTwoReturnSensorsMean = proxy_attribute(
        dtype=float,
        property_name="TempTwoReturnSensorsMeanSource",
        access=AttrWriteType.READ,
        description="This attribute specifies Temperature two return sensors mean"
    )

    TempFourReturnSensorsMean = proxy_attribute(
        dtype=float,
        property_name="TempFourReturnSensorsMeanSource",
        access=AttrWriteType.READ,
        description="This attribute specifies Temperature four return sensors mean"
    )

    TempSupplyPipeSensor = proxy_attribute(
        dtype=float,
        property_name="TempSupplyPipeSensorSource",
        access=AttrWriteType.READ,
        description="This attribute specifies Temperature supply pipe sensor"
    )

    TempReturnPipeSensor = proxy_attribute(
        dtype=float,
        property_name="TempReturnPipeSensorSource",
        access=AttrWriteType.READ,
        description="This attribute specifies Temperature return pipe sensor"
    )

    TempSurfaceSensorsMax = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensorsMaxSource",
        access=AttrWriteType.READ,
        description="This attribute specifies maximum temperature surface sensors"
    )

    TempSurfaceSensorsMin = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensorsMinSource",
        access=AttrWriteType.READ,
        description="This attribute specifies minimum temperature surface sensors"
    )

    TempSurfaceSensorsMean = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensorsMeanSource",
        access=AttrWriteType.READ,
        description="This attribute specifies Temperature surface sensors mean"
    )

    TempSurfaceSensor1= proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor1Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature surface sensor1"
    )

    TempSurfaceSensor2 = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor2Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature surface sensor2"
    )

    TempSurfaceSensor3 = proxy_attribute(
        dtype=float,
        property_name="TempSurfaceSensor3Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature surface sensor3"
    )

    TempSupplySensor1 = proxy_attribute(
        dtype=float,
        property_name="TempSupplySensor1Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature supply sensor1"
    )

    TempSupplySensor2 = proxy_attribute(
        dtype=float,
        property_name="TempSupplySensor2Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature supply sensor2"
    )

    TempReturnSensor1 = proxy_attribute(
        dtype=float,
        property_name="TempReturnSensor1Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature return sensor1"
    )

    TempReturnSensor2 = proxy_attribute(
        dtype=float,
        property_name="TempReturnSensor2Source",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature return sensor2"
    )

    TempSensorBeforeEV = proxy_attribute(
        dtype=float,
        property_name="TempSensorBeforeEVSource",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature sensor beforeEV"
    )

    TempSensorAfterEV = proxy_attribute(
        dtype=float,
        property_name="TempSensorAfterEVSource",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature sensor afterEV"
    )

    AtLeastTwoFaultySensors = proxy_attribute(
        dtype=float,
        property_name="AtLeastTwoFaultySensorsSource",
        access=AttrWriteType.READ,
        description="This attribute shows at least two faulty sensors"
    )

    MainSetpoint = proxy_attribute(
        dtype=float,
        property_name="MainSetpointSource",
        access=AttrWriteType.READ_WRITE,
        description="This attribute specifies main setpoint"
    )

    SensorControl = proxy_attribute(
        dtype=float,
        property_name="SensorControlSource",
        access=AttrWriteType.READ,
        description="This attribute specifies sensor control"
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

    SetpointAfterValve = proxy_attribute(
        dtype=float,
        property_name="SetpointAfterValveSource",
        access=AttrWriteType.READ_WRITE,
        description="This attribute specifies setpoint after valve"
    )

    SetpointAfterHeater = proxy_attribute(
        dtype=float,
        property_name="SetpointAfterHeaterSource",
        access=AttrWriteType.READ_WRITE,
        description="This attribute specifies setpoint after heater"
    )

    ChangeSetpoint = proxy_attribute(
        dtype=float,
        property_name="ChangeSetpointSource",
        access=AttrWriteType.READ_WRITE,
        description="This attribute changes setpoint"
    )

    ValveValue = proxy_attribute(
        dtype=float,
        property_name="ValveValueSource",
        access=AttrWriteType.READ,
        description="This attribute shows valve value"
    )

    HeaterValue = proxy_attribute(
        dtype=float,
        property_name="HeaterValueSource",
        access=AttrWriteType.READ,
        description="This attribute shows heater value"
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

    PlungerTempSensor = proxy_attribute(
        dtype=float,
        property_name="PlungerTempSensorSource",
        access=AttrWriteType.READ,
        description="This attribute specifies plunger temperature sensor"
    )

    StartPumpAttribute = proxy_attribute(
        dtype=bool,
        property_name="StartPumpSource",
        access=AttrWriteType.READ,
        description="This attribute starts the pump"
    )

    StopPumpAttribute = proxy_attribute(
        dtype=bool,
        property_name="StopPumpSource",
        access=AttrWriteType.READ,
        description="This attribute stops the pump"
    )

    ResetAttribute = proxy_attribute(
        dtype=bool,
        property_name="ResetSource",
        access=AttrWriteType.READ,
        description="This attribute resets the pump"
    )

    # Proxy commands

    @proxy_command(
        property_name="StartPumpSource",
        write_attribute=True)
    def StartPump(self, subcommand):
        """
        This command starts the pump.
        :param subcommand:
        :return:
        """
        subcommand(1)

    @proxy_command(
        property_name="StopPumpSource",
        write_attribute=True)
    def StopPump(self, subcommand):
        """
        This command stops the pump.
        :param subcommand:
        :return:
        """
        subcommand(1)

    @proxy_command(
        property_name="ResetSource",
        write_attribute=True)
    def Reset(self, subcommand):
        """
        This command resets the pump.
        :param subcommand:
        :return:
        """
        subcommand(1)


run=LandauSHG.run_server()

if __name__ == '__main__':
   run()
