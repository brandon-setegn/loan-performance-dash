from google.cloud import bigquery
import pandas as pd

from log_helper import log_execution_time

@log_execution_time
def get_performance():
    client = bigquery.Client()
    sql = """
        SELECT
            dq60plus/active_loan_count * 100 AS dlq60pct,
            dq90plus/active_loan_count * 100 AS dlq90pct,
            cpr,
            current_actual_upb,
            active_loan_count,
            reporting_period,
            deal_name
        FROM
            `cas_loanperf_dbt.cas_deals_perf`
        ORDER BY
            deal_name, reporting_period;
    """
    query_job = client.query(sql)
    df = query_job.to_dataframe()
    # rows = query_job.result()
    # # Convert the query result to a pandas DataFrame
    # df = pd.DataFrame(
    #     [(
    #         row.dlq60pct,
    #         row.dlq90pct,
    #         row.reporting_period, row.deal_name) for row in rows],
    #     columns=['dlq60pct', 'dlq90pct', 'reporting_period', 'deal_name']
    # )
    return df
