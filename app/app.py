import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import plotly.figure_factory as ff

data = pd.read_csv("Lounge_Occupancy_Count.csv") #extracting from data dump 
date = '1/3/19'
# time = '12am - 5am'
lounge_area = 'Occupancy Rate (Biz -Dining )'
# occupancy = data[ (data['Date']==date) & (data['Time'] == time ) ][lounge_area]


app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    html.Div([
        html.H1('Real Time Lounge Tracking System'),
        html.H2('Choose a lounge area'),
        dcc.Dropdown(
            id='area-dropdown',
            options =  [
                {'label': 'Biz -Dining', 'value':'Biz -Dining'},
                {'label': 'Biz - Workspace', 'value':'Biz - Workspace'},
                {'label': 'Biz - Main Lounge Area', 'value':'Biz - Main Lounge Area'},
                {'label': 'Biz - Zen Area', 'value':'Biz - Zen Area'},
                {'label': '1st - Dining', 'value':'1st - Dining'},
                {'label': '1st -Main Lounge Area', 'value':'1st -Main Lounge Area'},
                {'label': '1st - Workspace', 'value':'1st - Workspace'},
                {'label': 'Priv - Dining', 'value':'Priv - Dining'},
                {'label': 'Priv - -Main Lounge Area', 'value':'Priv - -Main Lounge Area'},
                {'label': 'Priv - Workspace', 'value':'Priv - Workspace'},
                {'label': 'Priv - Quiet Room', 'value':'Priv - Quiet Room'},
                {'label': 'Priv - Kids Room', 'value':'Priv - Kids Room'}],
            multi=False,
            value = 'Biz -Dining'
            
        ),
        html.Div(id = 'dd-output-container')
    ], style={'width': '40%', 'display': 'table','margin':'0 auto'})
])

@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('area-dropdown', 'value')])

def update_output(value):
    temp = 'Occupancy Rate ('+value+" )"
    return {
    'data': [go.Heatmap(
    x=data[(data['Date']==date)]['Time'],
    y=data[(data['Date']==date)][temp])]
    }



if __name__ == '__main__':
    app.run_server(debug=True)


