import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

from joblib import load
pipeline = load('assets/pipeline.joblib')

import plotly.graph_objects as go
import pandas as pd
bitcoin = pd.read_csv('bitcoin.csv')

bitcoin['string_date'] = bitcoin['Date'].copy()
bitcoin['Date'] = pd.to_datetime(bitcoin['Date'])
bitcoin['Year'] = bitcoin['Date'].dt.year
bitcoin['Month'] = bitcoin['Date'].dt.month
bitcoin['Day'] = bitcoin['Date'].dt.day

drop_columns = ['Date','Close**', 'Volume', 'Market Cap', 'High', 'Low']
new_bitcoin = bitcoin.drop(columns=drop_columns)

train = new_bitcoin[new_bitcoin.Year < 2016]
val = new_bitcoin[(new_bitcoin.Year > 2015) & (new_bitcoin.Year < 2018)]
test = new_bitcoin[new_bitcoin.Year >= 2013]

y_pred = pipeline.predict(test)
test['pred_price'] = y_pred

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Insights

            To the left, you'll see a Partial Dependence PLot.

            Essentially what it's saying is, as the opening price increases you'll expect 
            either higher prices, lower prices, or no change in prices. 
            (depending on what opening price you're looking at)

            If you look at the graph under the prediction tab,
            you'll notice that my model fits really well for years 2013 - 2017.
            However, for years 2018 - 2019, the model is not as tight.

            This likely due to the fall of bitcoin from Dec. 2017 - February 2018.

            """
        ),

    ],
    md=4,
)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=bitcoin.Date,
    y=bitcoin['Close**'],
    name='Closing Price',
    line_color = 'green',
    opacity=0.8)
    )

fig.add_trace(go.Scatter(
    x=bitcoin.Date,
    y=test['pred_price'],
    name='Predicted close',
    line_color = 'red',
    opacity=0.8)
    )

fig.update_layout(xaxis_range=['2013-04-28','2019-08-12'],
                    title_text='Bitcoin Historical Data')

column2 = dbc.Col(
    [
        html.Img(src='assets/PDP.png', className='img-fluid'),
        dcc.Graph(figure=fig)
    ]
)

layout = dbc.Row([column1, column2])