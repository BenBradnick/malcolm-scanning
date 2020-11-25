from typing import List, Union

from scanning.axisparams import AxisParams
from p4p import Type, Value
from p4p.client.thread import Context


context = Context("pva")


class Scan:

    configure_value = Value(Type([("method", "s")]), dict(method="configure"))
    abort_value = Value(Type([("method", "s")]), dict(method="abort"))
    reset_value = Value(Type([("method", "s")]), dict(method="reset"))

    def __init__(self, block_name: str) -> None:
        self.block_name = block_name
        self.context = context

    def reset(self) -> None:
        self.context.rpc(self.block_name, None, Scan.reset_value)

    def abort(self) -> None:
        self.context.rpc(self.block_name, None, Scan.abort_value)

    def run_scan(
        self,
        axes_params: Union[AxisParams, List[AxisParams]],
        duration: float,
        file_dir: str,
    ):
        self.report("Configuring scan...")

    def report(self, message):
        print(f"{self.block_name}: {message}")
