import logging

from rich.console import Console
from rich.table import Table
from typer import Typer

from utils import convert, load_rates

logging.basicConfig(
    level="INFO",
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)


app = Typer()
console = Console()


@app.command()
def exchange_rate(
    from_currency: str,
    to_currency: str,
    amount: float,
) -> None:
    exchange_rates = load_rates("rates.json")

    try:
        conversion_rate = convert(
            from_currency=from_currency,
            to_currency=to_currency,
            amount=amount,
            rates=exchange_rates,
        )
        print(conversion_rate)
    except ValueError as e:
        print(f"An error occurred: {e}")


@app.command()
def list_currencies() -> None:
    exchange_rates = load_rates("rates.json")

    table = Table("Code", "Name", "Rate", collapse_padding=True)
    for rate in exchange_rates.values():
        table.add_row(rate["code"], rate["name"], str(rate["rate"]))

    console.print(table)


if __name__ == "__main__":
    app()
