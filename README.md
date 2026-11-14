# PS-129: Esports Tournament Bracket, Seeding and Prize Split Engine with Penalties

## 1. Project Overview

This project aims to develop a Python-based backend engine for managing esports tournaments.

The planned system includes tournament data processing, team seeding, bracket generation, match processing, prize calculation and penalty handling.

## 2. Technologies Used

- Python
- Pandas
- Pytest
- Git
- GitHub

## 3. Project Structure

```text
T035-PS-129/
│
├── data/
│   ├── input/
│   └── output/
│
├── src/
│   ├── main.py
│   ├── input_reader.py
│   ├── validator.py
│   ├── seeding.py
│   ├── bracket.py
│   ├── match_processor.py
│   ├── prize_calculator.py
│   ├── penalty_handler.py
│   ├── output_generator.py
│   ├── config.py
│   ├── logger.py
│   └── exceptions.py
│
├── tests/
├── requirements.txt
└── README.md
```

## 4. Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 5. Running the Project

```bash
python src/main.py
```

## 6. Running Tests

```bash
python -m pytest -v
```

## 7. Development Status

- Project structure: Completed
- Python environment: Configured
- GitHub integration: Completed
- Logging: Implemented
- Input reading: Implemented
- Basic input validation: Implemented
- Custom exception handling: Implemented
- Tournament business rules: Pending official requirements

## 8. Team

Team ID: T035

Problem Statement: PS-129