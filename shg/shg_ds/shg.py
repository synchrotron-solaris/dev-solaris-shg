"""This is SHG device class based on the facadedevice library"""

from facadedevice import Facade, proxy_attribute, proxy_command
from tango import AttrWriteType, DevState


class SHG(Facade):


    def safe_init_device(self):
        """
        Docstring for 'safe_init_device' - it is just safe initialization of the DS
        :return:
        """
        super(SHG, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running")

    # Proxy attributes

    Temperature = proxy_attribute(
        dtype=float,
        property_name="TemperatureModbus",
        access=AttrWriteType.READ,
        description="This attribute specifies temperature"
    )

    TemperatureSetpoint = proxy_attribute(
        dtype=float,
        property_name="TemperatureSetpointModbus",
        access=AttrWriteType.READ_WRITE,
        description="This attribute specifies temperature setpoint"
    )

    SledSetpoint = proxy_attribute(
        dtype=float,
        property_name="SledSetpointModbus",
        access=AttrWriteType.READ_WRITE,
        description="This attribute specifies Sled setpoint"
    )

    SledMaster = proxy_attribute(
        dtype=float,
        property_name="SledMasterModbus",
        access=AttrWriteType.READ,
        description="This attribute specifies Sled master"
    )

    SledSlave = proxy_attribute(
        dtype=float,
        property_name="SledSlaveModbus",
        access=AttrWriteType.READ,
        description="This attribute specifies Sled slave"
    )

    SledHeaterOut = proxy_attribute(
        dtype=float,
        property_name="SledHeaterOutModbus",
        access=AttrWriteType.READ,
        description="This attribute specifies Sled heater OUT"
    )

    Linac1Setpoint = proxy_attribute(
        dtype=float,
        property_name="Linac1SetpointModbus",
        access=AttrWriteType.READ_WRITE,
        description="This attribute specifies Liniac1 setpoint"
    )

    Linac1Master = proxy_attribute(
        dtype=float,
        property_name="Linac1MasterModbus",
        access=AttrWriteType.READ,
        description="This attribute specifies Liniac1 master"
    )

    Linac1Slave = proxy_attribute(
        dtype=float,
        property_name="Linac1SlaveModbus",
        access=AttrWriteType.READ,
        description="This attribute specifies Liniac1 slave"
    )

    Linac1HeaterOut = proxy_attribute(
        dtype=float,
        property_name="Linac1HeaterOutModbus",
        access=AttrWriteType.READ,
        description="This attribute specifies Liniac1 heater OUT"
    )

    Linac2Setpoint = proxy_attribute(
        dtype=float,
        property_name="Linac2SetpointModbus",
        access=AttrWriteType.READ_WRITE,
        description="This attribute specifies Liniac2 setpoint"
    )

    Linac2Master = proxy_attribute(
        dtype=float,
        property_name="Linac2MasterModbus",
        access=AttrWriteType.READ,
        description="This attribute specifies Liniac2 master"
    )

    Linac2Slave = proxy_attribute(
        dtype=float,
        property_name="Linac2SlaveModbus",
        access=AttrWriteType.READ,
        description="This attribute specifies Liniac2 slave"
    )

    Linac2HeaterOut = proxy_attribute(
        dtype=float,
        property_name="Linac2HeaterOutModbus",
        access=AttrWriteType.READ,
        description="This attribute specifies Liniac2 heater OUT"
    )

    WaterSetpoint = proxy_attribute(
        dtype=float,
        property_name="WaterSetpointModbus",
        access=AttrWriteType.READ_WRITE,
        description="This attribute specifies water setpoint"
    )

    WaterIn = proxy_attribute(
        dtype=float,
        property_name="WaterInModbus",
        access=AttrWriteType.READ,
        description="This attribute shows water IN"
    )

    WaterOut = proxy_attribute(
        dtype=float,
        property_name="WaterOutModbus",
        access=AttrWriteType.READ,
        description="This attribute shows water OUT"
    )

    WaterAfterPump = proxy_attribute(
        dtype=float,
        property_name="WaterAfterPumpModbus",
        access=AttrWriteType.READ,
        description="This attribute shows water after the pump"
    )

    Valve = proxy_attribute(
        dtype=float,
        property_name="ValveModbus",
        access=AttrWriteType.READ,
        description="This attribute specifies valve state"
    )

    Sled2 = proxy_attribute(
        dtype=float,
        property_name="Sled2Modbus",
        access=AttrWriteType.READ,
        description="This attribute specifies sled"
    )

    Flow = proxy_attribute(
        dtype=float,
        property_name="FlowTag",
        access=AttrWriteType.READ,
        description="This attribute specifies flow"
    )

    Pressure = proxy_attribute(
        dtype=float,
        property_name="PressureTag",
        access=AttrWriteType.READ,
        description="This attribute specifies pressure"
    )

    PressureSetpoint = proxy_attribute(
        dtype=float,
        property_name="PressureSetpointTag",
        access=AttrWriteType.READ_WRITE,
        description="This attribute specifies pressure setpoint"
    )

    PressureAlarm = proxy_attribute(
        dtype=float,
        property_name="PressureAlarmTag",
        access=AttrWriteType.READ,
        description="This attribute indicates pressure alarm"
    )

    StartPump = proxy_attribute(
        dtype=bool,
        property_name="StartPumpTag",
        access=AttrWriteType.READ_WRITE,
        description="This attribute starts the pump"
    )

    StopPump = proxy_attribute(
        dtype=bool,
        property_name="StopPumpTag",
        access=AttrWriteType.READ_WRITE,
        description="This attribute stops the pump"
    )

    Reset = proxy_attribute(
        dtype=bool,
        property_name="ResetTag",
        access=AttrWriteType.READ_WRITE,
        description="This attribute resets the pump"
    )

    # Proxy commands

    @proxy_command(
        property_name="StartPumpTag",
        write_attribute=True)
    def StartPump(self, subcommand):
        """
        This command starts the pump.
        :param subcommand:
        :return:
        """
        subcommand(1)

    @proxy_command(
        property_name="StopPumpTag",
        write_attribute=True)
    def StopPump(self, subcommand):
        """
        This command stops the pump.
        :param subcommand:
        :return:
        """
        subcommand(1)

    @proxy_command(
        property_name="ResetPumpTag",
        write_attribute=True)
    def Reset(self, subcommand):
        """
        This command resets the pump.
        :param subcommand:
        :return:
        """
        subcommand(1)

if __name__ == '__main__':
    SHG.run_server()
