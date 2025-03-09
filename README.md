# Fetch Papers

## Overview
Fetch Papers is a command-line tool that retrieves research papers from PubMed based on a user-specified query. It filters papers with at least one author affiliated with a pharmaceutical or biotech company and saves the results as a CSV file.

## Features
- Fetches research papers using PubMed API.
- Identifies non-academic authors affiliated with pharmaceutical or biotech companies.
- Outputs results in CSV format.
- Command-line options for query input, debugging, and file output.

## Installation
### Prerequisites
- Python 3.13.1
- Poetry (for dependency management)

### Portry installation steps:
- For Linux
    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc   # For Bash users
    source ~/.bashrc
    ```
- For windows
    ```sh
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
    poetry --version
    ```
- If any while installing in windows any error occurs follow below steps
    ```sh
    echo $env:APPDATA\Python\Scripts
    $env:Path += ";$env:APPDATA\Python\Scripts"
    poetry --version
    ```

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone  https://github.com/REIKS18/webscrapping.git
   cd webscrapping
   ```
2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```
3. Run the tool:
   ```sh
    poetry run python -m fetch_papers.cli "biotech company"
    poetry run get-papers-list "biotech company" -f results.csv
   ```

## Usage
```sh
poetry run get-papers-list <query> [-f <filename>]
```
Options:
- `<query>`: Search term for fetching papers.
- `-f, --file <filename>`: Save results to a CSV file.
- `-h, --help`: Show help message.

## Example
```sh
poetry run get-papers-list "biotech company" -f biotech_company.csv
```

## Project Structure
```
webscrapping/
├── fetch_papers/
│   ├── __init__.py
│   ├── fetch.py  # Fetch and filter papers
│   ├── cli.py    # Command-line interface
├── README.md
├── pyproject.toml  # Poetry configuration
├── .gitignore
└── (other files)
```

## Dependencies
- `requests`: For API requests
- `lxml`: For XML parsing

## Contributing
1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch`
3. Commit changes: `git commit -m "Add new feature"`
4. Push to GitHub: `git push origin feature-branch`
5. Open a Pull Request

## License
