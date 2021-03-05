# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process
            
            This app is built on top of the idea for my first data storytelling project.
            I downloaded a list of Airbnb listings for the city of Seattle from insideairbnb.com and then used it to create
            a prediction app to predict the price of a typical Airbnb listing based on four promiment features 
            that were identified during the analysis.
            
            Because these listings were scraped of the airbnb website, certain features such as the number of bookings or
            revenue related data for these listings couldn't be obtained. As a result, using an evaluation metric that could
            be useful to the ML model was necessary. Since I am dealing with a regression problem here, i focused on the RSME. 
            
            Using a tree based model, i was able to list out the top 20 features that played a role in predicting the price.
            The top 4 features were then used to create a prediction app that is present on this website.
         

            """
        ),

    ],
)

layout = dbc.Row([column1])