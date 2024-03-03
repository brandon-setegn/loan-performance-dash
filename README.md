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


## Docker Image
The included Dockerfile will build an image that can be used to run the application.
1. Export Poetry to requirements.txt
```shell
poetry export --without-hashes -f requirements.txt -o requirements.txt
```
2. Build Docker image with tag
```shell
docker build -t loan-performance-dash .
```
3. Run Locally - this requires setting Google credentials to be able to connect to BigQuery
```shell
docker run -e GOOGLE_CLOUD_PROJECT={gcp-project-id} -e GOOGLE_APPLICATION_CREDENTIALS=/tmp/keys/application_default_credentials.json -v {path-to-local-application_default_credentials.json}:/tmp/keys/application_default_credentials.json -p 8000:8000 loan-performance-dash
```
