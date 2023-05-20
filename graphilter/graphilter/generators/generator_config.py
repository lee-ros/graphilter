import dataclasses
from dataclasses import dataclass, fields


@dataclass
class GeneratorConfig:
    outer_coeff: float = 1.0
    outer_offset: float = 0.0
    inner_coeff: float = 1.0
    inner_offset: float = 0.0
    power: float = 1.0