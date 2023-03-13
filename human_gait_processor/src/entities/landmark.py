from dataclasses import dataclass, field
from typing import NoReturn

from .landmark_coordinate import LandmarkCoordinate


@dataclass(init=True, repr=True)
class Landmark:
    name: str
    coordinate: LandmarkCoordinate
    angle: float = field(init=False)

    def calculate_angle(self, left_landmark, right_landmark) -> NoReturn:
        ...
