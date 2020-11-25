class AxisParams:
    def __init__(
        self, axis_name: str, units: str, start: float, stop: float, steps: int
    ):
        self.axis_name = axis_name
        self.units = units
        self.start = start
        self.stop = stop
        self.steps = steps
