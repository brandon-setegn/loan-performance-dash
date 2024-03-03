import dash
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash import dcc
from dash import html
import queries as q

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
app._favicon = "assets/favicon.ico"
app.title = "CAS - Loan Performance"

dq60 = q.get_dq60()
cpr = q.get_cpr()


app.layout = html.Div([
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
    ], style={'width': '50%', 'display': 'inline-block'}),
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
    ], style={'width': '50%', 'display': 'inline-block'})
])

if __name__ == '__main__':
    app.run_server(debug=True)
