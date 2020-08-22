import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.Div([
        html.H1('Price Optimization Dashboard'),
        html.H2('Choose a product name'),
        dcc.Dropdown(
            id='product-dropdown',
            options='dict_products',
            multi=True,
            value = ["Ben & Jerry's Wake and No Bake Cookie Dough Core Ice Cream","Brewdog Punk IPA"]
        ),
        dcc.Graph(
            id='product-like-bar'
        )
    ], style={'width': '40%', 'display': 'inline-block'}),
    html.Div([
        html.H2('All product info'),
        html.Table(id='my-table'),
        html.P(''),
    ], style={'width': '55%', 'float': 'right', 'display': 'inline-block'}),
    html.Div([
        html.H2('price graph'),
        dcc.Graph(id='product-trend-graph'),
        html.P('')
    ], style={'width': '100%',  'display': 'inline-block'})

])
if __name__ == '__main__':
    app.run_server(debug=True)


