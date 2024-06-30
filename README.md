# HL7-Data-Parsing-


# HL7 v2.x Message Parser and Analyzer

## Overview
This project develops a Python-based parser for HL7 v2.x messages, converting them into JSON format for analysis. It supports ADT, ORU, and ORM message types and includes error handling and logging.

## Project Structure
- `hl7_processing/`: Contains the main parser code and utility functions.
- `sample_data/`: Includes sample HL7 message files for testing.
- `tests/`: Contains unit tests for the parser.
- `logs/`: Stores logs for error messages.
- `requirements.txt`: Lists Python dependencies.

## Usage
1. Clone the repository and navigate to the project directory.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the parser on sample data: `python hl7_processing.py sample_data/adt_a01.hl7`.
4. View the JSON output and logs.


