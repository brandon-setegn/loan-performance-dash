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

dq60 = q.get_dq60()
cpr = q.get_cpr()

app.layout = html.Div([
    html.H1(children='Fannie Mae CAS - Loan Performance', style={'textAlign':'center'}),
    html.Div([
        dcc.Graph(
            id='dq-line-chart',
            figure={
                'data': [
                    go.Scatter(
                        x=dq60['reporting_period'],
                        y=dq60['dlq60pct'],
                        mode='lines',
                        name='DLQ 60%',
                        line=dict(color='darkred')
                    )
                ],
                'layout': go.Layout(
                    title='DLQ 60% over time',
                    xaxis={'title': 'Reporting Period'},
                    yaxis={'title': 'DLQ 60%'},
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
            id='cpr-line-chart',
            figure={
                'data': [
                    go.Scatter(
                        x=cpr['reporting_period'],
                        y=cpr['cpr'],
                        mode='lines',
                        name='CPR'
                    )
                ],
                'layout': go.Layout(
                    title='CPR over time',
                    xaxis={'title': 'Reporting Period'},
                    yaxis={'title': 'CPR'},
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
    app.run_server(debug=False)
