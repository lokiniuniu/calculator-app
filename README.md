# Calculator App

This is a simple calculator application that performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Project Structure

```
calculator-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── calculator.py    # Contains the Calculator class
│   └── utils.py         # Utility functions for input validation and formatting
├── tests
│   └── test_calculator.py # Unit tests for the Calculator class
├── requirements.txt     # Dependencies for the project
└── README.md            # Project documentation
```

## Installation

To get started, clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd calculator-app
```

Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the calculator application, execute the following command:

```bash
python src/main.py
```

Follow the prompts to perform calculations.

## Example

Here is a simple example of how to use the calculator:

1. Start the application.
2. Enter the first number.
3. Choose an operation (add, subtract, multiply, divide).
4. Enter the second number.
5. View the result.

## Running Tests

To ensure that the calculator functions correctly, you can run the unit tests:

```bash
python -m unittest discover -s tests
```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is open source and available under the MIT License.