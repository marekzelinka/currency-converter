import json
from typing import TypedDict


class Rate(TypedDict):
    code: str
    alphaCode: str
    numericCode: str
    name: str
    rate: float
    date: str
    inverseRate: float


def load_rates(filename: str) -> dict[str, Rate]:
    with open(filename) as file:
        return json.load(file)


def convert(*, amount: float, base: str, to: str, rates: dict[str, Rate]) -> float:
    base = base.lower()
    to = to.lower()

    from_rate = rates.get(base)
    to_rate = rates.get(to)
    if not to_rate:
        raise ValueError(f"Rate is invalid: to is {to}")

    if base == "eur":
        return amount * to_rate["rate"]

    if not from_rate:
        raise ValueError(f"Rate is invalid: base is {base}")

    return amount * (to_rate["rate"] / from_rate["rate"])


def main() -> None:
    # Load the currency rates
    rates = load_rates("rates.json")
    conversion = convert(amount=75, base="eur", to="dkk", rates=rates)
    print(conversion)


if __name__ == "__main__":
    main()
