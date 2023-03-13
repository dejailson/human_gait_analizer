from dataclasses import dataclass


@dataclass(init=True, repr=True)
class LandmarkCoordinate:
    x_axis: float
    y_axis: float
    z_axis: float
    visible: bool = False
