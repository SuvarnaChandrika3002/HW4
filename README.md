# Calculator CLI Application

A professional-grade **Python command-line calculator** with a REPL interface, modular design, full test coverage, and GitHub Actions CI/CD integration.  

This project demonstrates best practices in **software engineering**, including clean architecture, modularity, unit testing, input validation, error handling, and CI with coverage enforcement.  


##  Features

- **REPL (Read-Eval-Print Loop)** interface for continuous user interaction.  
- **Arithmetic operations**: Addition, Subtraction, Multiplication, Division.  
- **Special commands**:  
  - `help` → Show available commands.  
  - `history` → Show session calculation history.  
  - `exit` → Quit application.  
- **Input validation** & **error handling** (both LBYL & EAFP approaches).  
- **Calculation management** with history and factory design pattern.  
- **100% test coverage** with `pytest` and `pytest-cov`.  
- **CI/CD pipeline** using **GitHub Actions** enforcing coverage.  


##  Setup Instructions

### 1. Clone Repository
git clone https://github.com/<your-username>/calculator-cli.git
cd calculator-cli


### 2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   
venv\Scripts\activate      


### 3. Install Dependencies


pip install -r requirements.txt

*(Create `requirements.txt` with the following minimum content)*  

pytest
pytest-cov

##  Usage

Start the calculator REPL:


python -m app.calculator


Example interaction:


Welcome to the Calculator CLI!
Type 'help' for commands.

Operation: add
Enter numbers (comma separated): 10, 5
Result: 15.0

Operation: history
[1] 10 + 5 = 15.0

Operation: exit
Goodbye!

##  Testing

Run all tests with coverage:

pytest --cov=app tests/

Generate coverage report:

coverage report

Enforce **100% coverage** (CI will fail otherwise):

coverage report --fail-under=100

If you intentionally exclude lines (e.g., `pass`, `continue`), use:

```python
pass  # pragma: no cover
```

## GitHub Actions CI/CD

The project uses **GitHub Actions** to automatically:  

1. Install dependencies.  
2. Run unit tests with coverage.  
3. Enforce **100% coverage**.  

Workflow file: `.github/workflows/python-app.yml`

```yaml
name: Python application

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.x
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest pytest-cov
    - name: Run tests with coverage
      run: |
        pytest --cov=app tests/
    - name: Check coverage
      run: |
        coverage report --fail-under=100
```

- Fork the repo, create a branch, and make changes.  
- Ensure all tests pass (`pytest --cov=app tests/`).  
- Submit a PR with a clear description of changes.  




