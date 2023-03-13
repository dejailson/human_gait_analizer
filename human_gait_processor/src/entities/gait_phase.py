from dataclasses import dataclass


@dataclass(init=True, repr=True)
class GaitPhase:
    phase: str
    limb: str
