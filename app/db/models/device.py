from dataclasses import dataclass


@dataclass
class Device:
    id: str
    brand:str
    model:str
    os:str