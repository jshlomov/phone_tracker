from dataclasses import dataclass


@dataclass
class Device:
    id: str
    name: str
    brand: str
    model: str
    os: str