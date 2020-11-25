from typing import List, Union

from scanning.axisparams import AxisParams
from scanning.scan import Scan


def run_scan(
    scan_block: str,
    axes_params: Union[List[AxisParams], AxisParams],
    duration,
    file_dir,
) -> None:
    scan = Scan(scan_block)
    scan.run_scan(axes_params, duration, file_dir)


if __name__ == "__main__":
    fast_axis_params = AxisParams("stagex", "mm", 8.0, 10.0, 5)
    slow_axis_params = AxisParams("stagey", "mm", 8.0, 10.0, 5)
    scan_block = "BL45P-ML-MALC-01"
    axes_params = [fast_axis_params, slow_axis_params]
    duration = 0.1
    file_dir = "/dls/p45/data/2020/cm26482-5/tmp"

    run_scan(scan_block, axes_params, duration, file_dir)
