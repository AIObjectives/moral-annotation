
# Qualtrics Survey Formatter

This Python script automates the process of formatting a Qualtrics survey JSON template according to specific input data. It modifies survey questions, choices, and configurations to tailor the survey content for different scenarios, choices, and entity listings as defined by the user.

## Features

- **Dynamic Placeholder Replacement**: Replaces placeholders in the template with scenario-specific text and choices.
- **Outcome Looping**: Dynamically updates looping options based on outcomes listed in the input data.
- **Survey Renaming**: Automatically names surveys based on the input file to maintain uniqueness.
- **Custom Question Updates**: Adjusts consent and specific questions based on pre-defined criteria.

## Prerequisites

Before running this script, ensure you have Python installed on your machine. This script is tested with:

- Python 3.8 or higher

## Installation

Clone the repository to your local machine using:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd <project-directory>
```

It's recommended to create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required packages:

```bash
pip install typer
```

## Usage

To run the script, use the following command:

```bash
python process_survey.py --template path/to/your/template.json --input_dir path/to/input/jsons --output_dir path/to/output
```

### Arguments

- **template**: The path to the Qualtrics survey JSON template.
- **input_dir**: Directory containing input JSON files with data to integrate into the template.
- **output_dir**: Directory where the modified survey JSON files will be saved.

### Sample Command

```bash
python process_survey.py --template "templates/Annotation_Validation_Study_template.json" --input_dir "data/scenarios" --output_dir "output/surveys"
```

## How It Works

The script performs the following steps:

1. **Load the Survey Template**: Initializes the template from a JSON file.
2. **Process Each Input File**: For each JSON file in the input directory:
   - Replace text placeholders with actual data.
   - Update choices based on entities and outcomes.
   - Rename the survey based on the input file's name.
3. **Save the Formatted Survey**: Outputs the modified template into the designated output directory.
