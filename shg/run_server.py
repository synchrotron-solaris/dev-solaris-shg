"""
This module launches a Tango Device Server with three Device
Classes:

- `SHG`
- `RingSHG`
- `LandauSHG`

Entry point is already set, all you have to do is to define
`SHGDS` Device Server in your Tango Database
"""

from landau_shg_ds.landau_shg import LandauSHG
from ring_shg_ds.ring_shg import RingSHG
from shg_ds.shg import SHG
from tango.server import run

def main(args=None, **kwargs):
    return run({"SHG": SHG, "RingSHG": RingSHG, "LandauSHG":
                LandauSHG}, args=args,
               **kwargs)

if __name__ == '__main__':
    main()
