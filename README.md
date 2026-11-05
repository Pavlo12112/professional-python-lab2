# Data Processor

Laboratory work No. 2 for the course "Professional Python":
data structures and functional decomposition (variant 1,
analysis of student performance).

## Description

Module for processing structured data about students. It uses `list`,
`tuple`, `set`, `dict`, `Counter`, `defaultdict`, `deque`, comprehensions,
`*args`, `**kwargs`, `lambda`, closures and decorators.

## Requirements

Python 3.11+

## Installation

    python -m venv .venv

Activate the virtual environment
(Windows: `.venv\Scripts\activate`, Linux/macOS: `source .venv/bin/activate`).

    python -m pip install -e .

## Run

    python -m data_processor.main

Benchmark (list search versus dict index):

    python -m data_processor.benchmark

Tests:

    python -m unittest discover -s tests -v

## Project structure

- `src/data_processor/data.py` - input data (list, tuples).
- `src/data_processor/processors.py` - filter, search, group, count.
- `src/data_processor/analytics.py` - aggregation, sorting, closures.
- `src/data_processor/decorators.py` - decorators.
- `src/data_processor/benchmark.py` - list versus dict benchmark.
- `src/data_processor/main.py` - entry point.
- `tests/` - unit tests.

## Author

Student: Tsiastun Pavlo
Group: FeP-33s
