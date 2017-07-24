from facadedevice import Facade, proxy_attribute, proxy_command
from tango import AttrWriteType, DevState


class SHG(Facade):

    def safe_init_device(self):
        super(SHG, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running")

    # Proxy attributes

    Temperature = proxy_attribute(
        dtype=float,
        property_name="TemperatureModbus",
        access=AttrWriteType.READ
    )

    TemperatureSetpoint = proxy_attribute(
        dtype=float,
        property_name="TemperatureSetpointModbus",
        access=AttrWriteType.READ_WRITE
    )

    SledSetpoint = proxy_attribute(
        dtype=float,
        property_name="SledSetpointModbus",
        access=AttrWriteType.READ_WRITE
    )

    SledMaster = proxy_attribute(
        dtype=float,
        property_name="SledMasterModbus",
        access=AttrWriteType.READ
    )

    SledSlave = proxy_attribute(
        dtype=float,
        property_name="SledSlaveModbus",
        access=AttrWriteType.READ
    )

    SledHeaterOut = proxy_attribute(
        dtype=float,
        property_name="SledHeaterOutModbus",
        access=AttrWriteType.READ
    )

    Linac1Setpoint = proxy_attribute(
        dtype=float,
        property_name="Linac1SetpointModbus",
        access=AttrWriteType.READ_WRITE
    )

    Linac1Master = proxy_attribute(
        dtype=float,
        property_name="Linac1MasterModbus",
        access=AttrWriteType.READ
    )

    Linac1Slave = proxy_attribute(
        dtype=float,
        property_name="Linac1SlaveModbus",
        access=AttrWriteType.READ
    )

    Linac1HeaterOut = proxy_attribute(
        dtype=float,
        property_name="Linac1HeaterOutModbus",
        access=AttrWriteType.READ
    )

    Linac2Setpoint = proxy_attribute(
        dtype=float,
        property_name="Linac2SetpointModbus",
        access=AttrWriteType.READ_WRITE
    )

    Linac2Master = proxy_attribute(
        dtype=float,
        property_name="Linac2MasterModbus",
        access=AttrWriteType.READ
    )

    Linac2Slave = proxy_attribute(
        dtype=float,
        property_name="Linac2SlaveModbus",
        access=AttrWriteType.READ
    )

    Linac2HeaterOut = proxy_attribute(
        dtype=float,
        property_name="Linac2HeaterOutModbus",
        access=AttrWriteType.READ
    )

    WaterSetpoint = proxy_attribute(
        dtype=float,
        property_name="WaterSetpointModbus",
        access=AttrWriteType.READ_WRITE
    )

    WaterIn = proxy_attribute(
        dtype=float,
        property_name="WaterInModbus",
        access=AttrWriteType.READ
    )

    WaterOut = proxy_attribute(
        dtype=float,
        property_name="WaterOutModbus",
        access=AttrWriteType.READ
    )

    WaterAfterPump = proxy_attribute(
        dtype=float,
        property_name="WaterAfterPumpModbus",
        access=AttrWriteType.READ
    )

    Valve = proxy_attribute(
        dtype=float,
        property_name="ValveModbus",
        access=AttrWriteType.READ
    )

    Sled2 = proxy_attribute(
        dtype=float,
        property_name="Sled2Modbus",
        access=AttrWriteType.READ
    )

    Flow = proxy_attribute(
        dtype=float,
        property_name="FlowTag",
        access=AttrWriteType.READ
    )

    Pressure = proxy_attribute(
        dtype=float,
        property_name="PressureTag",
        access=AttrWriteType.READ
    )

    PressureSetpoint = proxy_attribute(
        dtype=float,
        property_name="PressureSetpointTag",
        access=AttrWriteType.READ_WRITE
    )

    PressureAlarm = proxy_attribute(
        dtype=float,
        property_name="PressureAlarmTag",
        access=AttrWriteType.READ
    )

    StartPump = proxy_attribute(
        dtype=bool,
        property_name="StartPumpTag",
        access=AttrWriteType.READ_WRITE
    )

    StopPump = proxy_attribute(
        dtype=bool,
        property_name="StopPumpTag",
        access=AttrWriteType.READ_WRITE
    )

    Reset = proxy_attribute(
        dtype=bool,
        property_name="ResetTag",
        access=AttrWriteType.READ_WRITE
    )

    # Proxy commands

    @proxy_command(
        property_name="StartPumpTag",
        write_attribute=True)
    def StartPump(self, subcommand):
        subcommand(1)

    @proxy_command(
        property_name="StopPumpTag",
        write_attribute=True)
    def StopPump(self, subcommand):
        subcommand(1)

    @proxy_command(
        property_name="ResetPumpTag",
        write_attribute=True)
    def Reset(self, subcommand):
        subcommand(1)



if __name__ == '__main__':
   SHG.run_server()