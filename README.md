# Currency converter CLI

Currency conversion cli made using **Python** and **Typer**.

## Setup

This project uses the modern `pyproject.toml` standard for dependency management and requires the `uv` tool to manage the environment.

```sh
uv sync
```

## Usage

```sh
uv run main.py list-currencies # Lists available currencies
uv run main.py exchange-rate eur dkk 70 # Converts 70 Euros to Danish Krone
```
