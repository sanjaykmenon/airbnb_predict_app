# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predicting Airbnb Prices

            This app helps you predict Airbnb prices in the Seattle area based on the following parameters:
            
            -   Bedrooms
            -   Bathrooms
            -   Cleaning Fee
            -   Number of days an Airbnb Host has been active on the platform.

            

            """
        ),
        dcc.Link(dbc.Button('Click Here to Predict Prices', color='primary'), href='/predictions')
    ],
    md=4,
)

df = pd.read_csv('df.csv')
fig = px.scatter(df,x=df['host_days'], y=df['first_review_days'], opacity = 0.3
             ,title='Host Active Days vs. First Review Days')
fig.update_xaxes(range=[0, 4000])
fig.update_yaxes(range=[0, 4000])
fig.update_layout(
    xaxis_title="Number of Days Host has been Active on Airbnb",
    yaxis_title="Number of Days since the first review"
    )
column2 = dbc.Col(
    [
        #html.Img(src='assets/days_reviews.png', className='img-fluid')
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])