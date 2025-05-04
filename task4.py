import numpy as np 
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

daily_sales_data = pd.read_csv('data/daily_sales_data.csv')
daily_sales_data_north=daily_sales_data[daily_sales_data['region']== 'north']
daily_sales_data_south=daily_sales_data[daily_sales_data['region']== 'south']
daily_sales_data_east=daily_sales_data[daily_sales_data['region']== 'east']
daily_sales_data_west=daily_sales_data[daily_sales_data['region']== 'west']
daily_sales_data_all=daily_sales_data.copy()



#task3
# app = dash.Dash(__name__)
# app.layout = html.Div([
#     html.H1("Sales Data Visualization"),
#     dcc.Graph(
#         id='sales-graph',
#         figure=px.line(daily_sales_data, x='date', y='Sales', title='Sales Over Time')
#     )
# ])
# if __name__ == '__main__':
#     app.run(debug=True)


#task4
app = dash.Dash(__name__)
app.layout = html.Div([
    html.Link(rel='stylesheet', href='/assets/style.css'),
    html.H1("Sales Data Visualization"),
    dcc.RadioItems(
    id='regionwise-graph',
    options=[
        {'label': 'North', 'value': 'North'},
        {'label': 'South', 'value': 'South'},
        {'label': 'East', 'value': 'East'},
        {'label': 'West', 'value': 'West'},
        {'label': 'All', 'value': 'All'}
    ],
    value='All',
    labelStyle={'display': 'inline-block'},
    style={'margin-bottom': '20px', 'color': 'blue', 'font-size': '20px'}
    ),
    dcc.Graph(
        id='sales-graph',
        figure=px.line(daily_sales_data, x='date', y='Sales', title='Sales Over Time')
    )
])

@app.callback(
    Output('sales-graph', 'figure'),
    Input('regionwise-graph', 'value')
)
def update_graph(selected_region):
    if selected_region == 'North':
        filtered_data = daily_sales_data_north
    elif selected_region == 'South':
        filtered_data = daily_sales_data_south
    elif selected_region == 'East':
        filtered_data = daily_sales_data_east
    elif selected_region == 'West':
        filtered_data = daily_sales_data_west
    else:
        filtered_data = daily_sales_data_all

    fig = px.line(filtered_data, x='date', y='Sales', title=f'Sales Over Time - {selected_region} Region')
    return fig

if __name__ == '__main__':
    app.run(debug=True)
