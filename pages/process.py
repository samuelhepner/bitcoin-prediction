import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            Bitcoin can be difficult to predict especially if you don't use a computer and if you're simply using speculation. 
            I didn't want to speculate so I built this model to get a more accurate prediction.

            Unfortunately, I didn't have a lot of time so I wasn't able to do future predictions but, who knows, maybe that'll change.

            This web app uses a RandomForestRegressor to predict the price of Bitcoin using data from [Coin Market Cap](https://coinmarketcap.com/currencies/bitcoin/historical-data/).

            I tried to do some feature engineering but surprisingly, most of them didn't help my prediction, so I decided to stick with the data that was given to me.
            In the data was the opening price, closing price, high daily price, low daily price, volume, market cap, and date.

            When I did my predictions, I removed closing price, high daily price, low daily price, volume, market cap. Thus, I was left with the date and the opening price. 
            I also did some feature engineering to get day, month, and year, individually (trust me, it helped).
             

            """
        ),

    ],
)

layout = dbc.Row([column1])