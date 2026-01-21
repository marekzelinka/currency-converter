import json
import logging
from typing import TypedDict

logging.basicConfig(
    level="INFO",
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)


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


def convert(
    *, from_currency: str, to_currency: str, amount: float, rates: dict[str, Rate]
) -> float:
    from_currency = from_currency.lower()
    to_currency = to_currency.lower()

    from_rate = rates.get(from_currency)
    to_rate = rates.get(to_currency)
    if not to_rate:
        raise ValueError(f"Rate is invalid: to is {to_currency}")

    if from_currency == "eur":
        return amount * to_rate["rate"]

    if not from_rate:
        raise ValueError(f"Rate is invalid: base is {from_currency}")

    return amount * (to_rate["rate"] / from_rate["rate"])


def main() -> None:
    # Load the currency rates
    rates = load_rates("rates.json")
    conversion = convert(from_currency="eur", to_currency="dkk", amount=75, rates=rates)
    print(conversion)


if __name__ == "__main__":
    main()
