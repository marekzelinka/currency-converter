import json
import logging

from models import Rate


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
