from google.cloud import bigquery
import pandas as pd

def get_dq60():
    client = bigquery.Client()
    sql = """
        SELECT dq60plus/active_loan_count * 100 as dlq60pct, reporting_period 
        FROM `cas_loanperf_dbt.cas_2022_r01_g1_perf`
        ORDER BY reporting_period
    """
    query_job = client.query(sql)
    rows = query_job.result()
    # Convert the query result to a pandas DataFrame
    df = pd.DataFrame(
        [(row.dlq60pct, row.reporting_period) for row in rows],
        columns=['dlq60pct', 'reporting_period']
    )
    return df

def get_cpr():
    client = bigquery.Client()
    sql = """
        SELECT cpr, reporting_period 
        FROM `cas_loanperf_dbt.cas_2022_r01_g1_perf`
        ORDER BY reporting_period
    """
    query_job = client.query(sql)
    rows = query_job.result()
    # Convert the query result to a pandas DataFrame
    df = pd.DataFrame(
        [(row.cpr, row.reporting_period) for row in rows],
        columns=['cpr', 'reporting_period']
    )
    return df
