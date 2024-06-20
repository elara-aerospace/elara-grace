# elara-grace: Elara Aerospace's Rocket Monitoring System

[![CodeFactor](https://www.codefactor.io/repository/github/elara-aerospace/elara-grace/badge)](https://www.codefactor.io/repository/github/elara-aerospace/elara-grace)

This module monitors the rocket's systems for anomalies or failures and initiates appropriate contingency actions or aborts if necessary.

## Project Naming

We named our debugging software after the first programmer who debugged code: Grace Hopper.
In 1945, while working on the Harvard Mark II computer, she discovered an actual moth causing a malfunction,
which she documented as the first "bug" in a computer system.
This incident led to the term "debugging" being coined to describe the process of identifying and fixing issues in computer code.

## Project Structure

- `src/`: Main source code
  - `rocket_systems/`: Modules for sensors, actuators, and communications
  - `monitoring/`: Modules for anomaly detection and contingency actions
- `tests/`: Unit tests
- `config/`: Configuration settings
- `logs/`: Log files
- `requirements.txt`: Python dependencies

## Usage

1. **Install dependencies:** Run `make` or `make install` to install the required packages.
2. **Run the tests:** Use `python3 -m unittest discover tests` to run the unit tests.
3. **Execute the main program:** Run `python3 src/main.py` to start the rocket monitoring system.

## Development

To test if your Python code is written according to best practices, please run `pylint` in your terminal:

        pylint src/*.py

## License

Copyright (c) 2024, Suriyaa Sundararuban (Head of Digital Operations at Elara Aerospace)
Copyright (c) 2024, Elara Aerospace team
