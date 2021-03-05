# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
pipeline=load('assets/model2.joblib')
# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### Bedrooms'),
        dcc.Slider(
            id='bedrooms',
            min=1,
            max=10,
            step=1,
            value=1,
            marks={n: str(n) for n in range(1,10,1)},
            className='mb-5',
        ),
        dcc.Markdown('#### Bathrooms'),
        dcc.Slider(
            id='bathrooms',
            min=1,
            max=10,
            step=1,
            value=1,
            marks={n: str(n) for n in range(1,10,1)},
            className='mb-5',
        ),
        dcc.Markdown('#### Number of Days Host has been Active'),
        dcc.Slider(
            id='host_days',
            min=50,
            max=2000,
            step=250,
            value=50,
            marks={n: str(n) for n in range(50, 2000, 250)},
            className='mb-5',
        ),

        dcc.Markdown('#### Cleaning Fee'),
        dcc.Dropdown(
            id='cleaning_fee',
            options = [
                {'label': '$50', 'value': '50'},
                {'label': '$75', 'value': '75'},
                {'label': '$100', 'value': '100'},
                {'label': '$125', 'value': '125'},
                {'label': '$150', 'value': '150'},
            ],
            value = '50',
            className='mb-5',
        ),

    ],
    md=4,

)

column2 = dbc.Col(
    [
        html.H2('Predicted Price of an Airbnb', className='mb-5'),
        html.Div(id='prediction-content', className='lead')
    ]
)

import pandas as pd
import shap

@app.callback(
    Output('prediction-content', 'children'),
    [Input('bedrooms', 'value'), Input('bathrooms', 'value'), Input('cleaning_fee', 'value'), Input('host_days', 'value') ],
)
def predict(bedrooms, bathrooms, cleaning_fee, host_days):
    # Make df from inputs
    df = pd.DataFrame(
        data=[[bedrooms, bathrooms, cleaning_fee, host_days]],
        columns=['bedrooms', 'bathrooms', 'cleaning_fee', 'host_days']
    )

    # Make a prediction
    model = load('assets/model2.joblib')
    pred = model.predict(df)[0]

    # Calculate the shap values
    #explainer = shap.TreeExplainer(model)
    #shap_values = explainer.shap_values(df)

    # Print some results
    #feature_names = df.columns
    #feature_values = df.values[0]
    #shaps = pd.Series(shap_values[0], zip(feature_names, feature_values))

    result = f'${pred:,.0f} is the estimated rent for this Airbnb. \n\n'
    #result += f'Starting from baseline of ${explainer.expected_value:,.0f} \n'
    #result += shaps.to_string()
    return result



layout = dbc.Row([column1, column2])
