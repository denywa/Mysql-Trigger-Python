# TRIGGER-DB Python Script Documentation

## Overview
This documentation provides an overview of the `TRIGGER-DB.py` Python script which is designed to interact with a MySQL database to manage student records and automatically calculate grades based on scores.

## Features
- **Database Connection**: Establishes a connection to a MySQL database.
- **Table Creation**: Creates a table named `mahasiswa` if it does not already exist. This table includes columns for student ID (NIM), name, score, and grade.
- **Triggers**:
  - **Before Insert Trigger**: Automatically calculates and sets the grade before a new record is inserted into the `mahasiswa` table based on the score.
  - **Before Update Trigger**: Automatically recalculates and updates the grade before a record in the `mahasiswa` table is updated.

## Schema of `mahasiswa` Table
- `NIM`: INT, Primary Key
- `Nama`: VARCHAR(100)
- `Nilai`: INT
- `Grade`: CHAR(2)

## Grade Calculation
The grade is calculated based on the `Nilai` (score) field as follows:
- 90 and above: A
- 85 to 89: A-
- 80 to 84: B+
- 75 to 79: B
- 70 to 74: B-
- 60 to 69: C+
- 55 to 59: C
- 45 to 54: D
- Below 45: E

## Usage
To use this script, ensure you have MySQL installed and configured correctly with a database named `trigger`. Update the connection parameters in the script if necessary. Run the script to set up the database schema and triggers automatically.

## Closing Connection
The script ensures that the database connection is closed properly after operations are completed to prevent any resource leaks.

## Note
This script is intended for educational purposes and demonstrates the use of triggers in MySQL through Python. Modify it according to your specific requirements.
