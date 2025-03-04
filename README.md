# ETL Project with Python and MySQL

A beginner's guide to extracting data from a CSV file, transforming it, and loading it into a MySQL database using Python.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)

## Introduction
This project demonstrates a simple ETL (Extract, Transform, Load) process where data is extracted from a CSV file, transformed (e.g., data cleaning and formatting), and loaded into a MySQL database. 

## Project Structure
project-directory/
├── createCSV.py
├── data_pipeline.py
├── data.csv
├── requirements.txt
└── README.md

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Frz-profile/MySQL_ETL_Pipeline.git
    ```
2. Navigate to the project directory:
    ```bash
    cd MySQL_ETL_Pipeline
    ```
3. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Create the CSV File:**
    ```bash
    python createCSV.py
    ```
2. **Create and Populate the Database:**
    ```bash
    python data_pipeline.py
    ```
