from dataclasses import dataclass
from typing import List

from .frame import Frame


@dataclass(init=True, repr=True)
class Video:
    name: str
    description: str
    frames: list[Frame]
