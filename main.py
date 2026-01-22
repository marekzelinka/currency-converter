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

    if from_currency == "eur":
        if not to_rate:
            raise ValueError(f"Currency code: {to_currency!r} is invalid.")
        return amount * to_rate["rate"]

    if to_currency == "eur":
        if not from_rate:
            raise ValueError(f"Currency code: {from_currency!r} is invalid.")
        return amount * from_rate["inverseRate"]

    if not to_rate:
        raise ValueError(f"Currency code: {to_currency!r} is invalid.")

    if not from_rate:
        raise ValueError(f"Currency code: {from_currency!r} is invalid.")

    rate = to_rate["rate"] / from_rate["rate"]
    result = amount * rate

    logging.info(f"Using rate {rate}")

    return result


def main() -> None:
    # Load the currency rates
    rates = load_rates("rates.json")
    try:
        # Get the conversion result
        conversion = convert(
            from_currency="dkk", to_currency="aud", amount=75, rates=rates
        )
        print(conversion)
    except ValueError as e:
        print(f"An error occurred: {e}.")


if __name__ == "__main__":
    main()
