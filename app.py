import logging

import dash
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import queries as q
from dash import dcc, html
from flask import request
from log_helper import setup_logging

setup_logging()
logging.info('Starting the app')


app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

# The server is needed when running in a docker image
server = app.server

app._favicon = "assets/favicon.ico"
app.title = "CAS - Loan Performance"

# Log every request for troubleshooting
@app.server.before_request
def log_request_info():
    logging.debug('Request: %s', extra={'host': request.host, 'path': request.path})

perf = q.get_performance()

app.layout = html.Div([
    html.H1(children='Fannie Mae CAS - Loan Performance', style={'textAlign':'center'}),
    html.Div([
        dcc.Graph(
            id='cpr-line-chart',
            figure={
                'data': [
                    go.Scatter(
                        x=perf[perf['deal_name'] == deal]['reporting_period'],
                        y=perf[perf['deal_name'] == deal]['cpr'],
                        mode='lines',
                        name=deal
                    )
                    for deal in perf['deal_name'].unique()
                ],
                'layout': go.Layout(
                    title='CPR',
                    xaxis={'title': 'Reporting Period'},
                    yaxis={'title': 'CPR'},
                )
            }
        )
    ], style={
        'width': 'calc(50% - 20px)',
        'display': 'inline-block',
        'margin': '10px'
        }),
    html.Div([
        dcc.Graph(
            id='cnt-line-chart',
            figure={
                'data': [
                    go.Scatter(
                        x=perf[perf['deal_name'] == deal]['reporting_period'],
                        y=perf[perf['deal_name'] == deal]['current_actual_upb'],
                        mode='lines',
                        name=deal
                    )
                    for deal in perf[(perf['deal_name'] != 'all_deals')]['deal_name'].unique()
                ],
                'layout': go.Layout(
                    title='Current UPB',
                    xaxis={'title': 'Reporting Period'},
                    yaxis={'title': 'UPB'},
                )
            }
        )
    ], style={
        'width': 'calc(50% - 20px)',
        'display': 'inline-block',
        'margin': '10px'
        }),
    html.Div([
        dcc.Graph(
            id='dq60-line-chart',
            figure={
                'data': [
                    go.Scatter(
                        x=perf[perf['deal_name'] == deal]['reporting_period'],
                        y=perf[perf['deal_name'] == deal]['dlq60pct'],
                        mode='lines',
                        name=deal
                    )
                    for deal in perf['deal_name'].unique()
                ],
                'layout': go.Layout(
                    title='DLQ 60+ % by Count',
                    xaxis={'title': 'Reporting Period'},
                    yaxis={'title': 'DLQ 60+ %', 'ticksuffix': '%'},
                )
            }
        )
    ], style={
        'width': 'calc(50% - 20px)',
        'display': 'inline-block',
        'margin': '10px'
        }),
    html.Div([
        dcc.Graph(
            id='dq90-line-chart',
            figure={
                'data': [
                    go.Scatter(
                        x=perf[perf['deal_name'] == deal]['reporting_period'],
                        y=perf[perf['deal_name'] == deal]['dlq90pct'],
                        mode='lines',
                        name=deal
                    )
                    for deal in perf['deal_name'].unique()
                ],
                'layout': go.Layout(
                    title='DLQ 90% by Count',
                    xaxis={'title': 'Reporting Period'},
                    yaxis={'title': 'DLQ 90+ %', 'ticksuffix': '%'},
                )
            }
        )
    ], style={
        'width': 'calc(50% - 20px)',
        'display': 'inline-block',
        'margin': '10px'
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)
