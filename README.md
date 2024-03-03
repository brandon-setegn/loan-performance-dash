# Loan Performance Dashboard

This project is a loan performance dashboard built using Poetry, Plotly Dash, and Google BigQuery.

## Dependencies

- [Poetry](https://python-poetry.org/): Dependency management and packaging tool for Python.
- [Plotly Dash](https://plotly.com/dash/): Python framework for building interactive web applications.
- [Google BigQuery](https://cloud.google.com/bigquery): Fully managed, serverless data warehouse by Google Cloud.

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/brandon/loan-performance-dash.git
    ```

2. Install project dependencies using Poetry:

    ```shell
    cd loan-performance-dash
    poetry install
    ```

## Usage

1. Set up your Google BigQuery credentials by following the instructions in the [Google Cloud documentation](https://cloud.google.com/bigquery/docs/reference/libraries).

2. Run the application:

    ```shell
    poetry run python app.py
    ```

3. Open your web browser and navigate to `http://localhost:8050` to access the loan performance dashboard.

## Contributing

Contributions are welcome! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).