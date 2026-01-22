from typing import TypedDict


class Rate(TypedDict):
    code: str
    alphaCode: str
    numericCode: str
    name: str
    rate: float
    date: str
    inverseRate: float
