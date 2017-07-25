"""Module to run the server."""

# Imports
import sys
from SHG.SHG import SHG
from RingSHG import RingSHG
from LandauSHG import LandauSHG

#: Server name as used in the Tango database
SHG_NAME = SHG.__class__
run_SHG = SHG.run_server

#: Server name as used in the Tango database
RingSHG_NAME = RingSHG.RingSHG.__class__
run_RingSHG = SHG.run_server

#: Server name as used in the Tango database
LandauSHG_NAME = LandauSHG.LandauSHG.__class__
run_LandauSHG = SHG.run_server


# Run function
def run(args=None, scope="", **kwargs):
    """Run an oscilloscope from a given scope type.
    It is based on the PyTango.server.run method.
    The diffrence is that the device class
    and server name are automatically given.
    Args:
        args (iterable): args as given in the PyTango.server.run method
                         without the server name. If None, the sys.argv
                         list is used
        scope (str): "RTO", "RTM" or "" to use sys.argv instead
        kwargs: the other keywords argument are as given
                in the PyTango.server.run method.
    """
    # SHG run
    try:
        if scope.lower() != "shg":
            sys.argv.remove("--shg")
        return run_SHG(args, **kwargs)
    except ValueError:
        pass
    # Ring run
    try:
        if scope.lower() != "ring":
            sys.argv.remove("--ring")
        return run_RingSHG(args, **kwargs)
    except ValueError:
        pass
    # Landau run
    try:
        if scope.lower() != "landau":
             sys.argv.remove("--landau")
        return run_LandauSHG(args, **kwargs)
    except ValueError:
        pass
    # Help
    if scope is not None:
        raise ValueError("Not a valid scope.")
    print("Use --shg or --ring or --landau options to select the scope type")


# Main execution
if __name__ == "__main__":
    run()