import dataclasses
from dataclasses import dataclass, fields


@dataclass
class GeneratorConfig:
    amplitude: float = 1.0
    y_offset: float = 0.0
    frequency: float = 1.0
    phase: float = 0.0
    power: float = 1.0