import logging

from typer import Typer

from utils import convert, load_rates

logging.basicConfig(
    level="INFO",
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)

app = Typer()


@app.command()
def exchange_rate(
    from_currency: str,
    to_currency: str,
    amount: float,
) -> None:
    # Load the currency rates
    rates = load_rates("rates.json")

    try:
        # Get the conversion result
        conversion = convert(
            from_currency=from_currency,
            to_currency=to_currency,
            amount=amount,
            rates=rates,
        )
        print(conversion)
    except ValueError as e:
        print(f"An error occurred: {e}.")


if __name__ == "__main__":
    app()
