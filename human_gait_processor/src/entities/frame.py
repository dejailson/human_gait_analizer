from dataclasses import dataclass
from typing import List

from .gait_phase import GaitPhase
from .landmark import Landmark


@dataclass(init=True, repr=True)
class Frame:
    elapsed_time: float
    landmarks: List[Landmark]
    gait_phases: List[GaitPhase]
