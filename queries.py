from google.cloud import bigquery
import pandas as pd

from log_helper import log_execution_time

@log_execution_time
def get_dq60():
    client = bigquery.Client()
    sql = """
        SELECT
            dq60plus/active_loan_count * 100 AS dlq60pct,
            reporting_period,
            deal_name
        FROM
            `cas_loanperf_dbt.cas_deals_perf`
        ORDER BY
            deal_name, reporting_period;
    """
    query_job = client.query(sql)
    rows = query_job.result()
    # Convert the query result to a pandas DataFrame
    df = pd.DataFrame(
        [(row.dlq60pct, row.reporting_period, row.deal_name) for row in rows],
        columns=['dlq60pct', 'reporting_period', 'deal_name']
    )
    return df

@log_execution_time
def get_cpr():
    client = bigquery.Client()
    sql = """
        SELECT
            cpr,
            reporting_period,
            deal_name
        FROM
            `cas_loanperf_dbt.cas_deals_perf`
        ORDER BY
            deal_name, reporting_period;
    """
    query_job = client.query(sql)
    rows = query_job.result()
    # Convert the query result to a pandas DataFrame
    df = pd.DataFrame(
        [(row.cpr, row.reporting_period, row.deal_name) for row in rows],
        columns=['cpr', 'reporting_period', 'deal_name']
    )
    return df
