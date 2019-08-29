import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

from app import app
import pandas as pd
bitcoin = pd.read_csv('bitcoin.csv')

bitcoin['string_date'] = bitcoin['Date'].copy()
bitcoin['Date'] = pd.to_datetime(bitcoin['Date'])
bitcoin['Year'] = bitcoin['Date'].dt.year
bitcoin['Month'] = bitcoin['Date'].dt.month
bitcoin['Day'] = bitcoin['Date'].dt.day

drop_columns = ['Date','Close**', 'Volume', 'Market Cap', 'High', 'Low']
new_bitcoin = bitcoin.drop(columns=drop_columns)

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Bitcoin Historical Data

            This app will do its best to predict bitcoin prices. 
            This app will not predict the future price of Bitcoin.

            On the right, there's a Plotly graph of bitcoin's historical 
            high and low prices for every day in the data.

            If you have any comments or questions feel free to click 
            one of the boxes below to get in contact with me.

            """
        ),
        dcc.Link(dbc.Button('Predictions', color='primary'), href='/predictions')
    ],
    md=4,
)

import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(
                x=bitcoin.Date,
                y=bitcoin['High'],
                name='BTC High',
                line_color = 'green',
                opacity=0.8)
             )

fig.add_trace(go.Scatter(
                x=bitcoin.Date,
                y=bitcoin['Low'],
                name='BTC Low',
                line_color = 'red',
                opacity=0.8)
             )

fig.update_layout(xaxis_range=['2013-04-28','2019-08-12'],
                 title_text='Bitcoin Historical High and Low Data')

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])