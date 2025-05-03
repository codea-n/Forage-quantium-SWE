import numpy as np 
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px


#task 2
daily_sales_data_0 = pd.read_csv('data/daily_sales_data_0.csv')
daily_sales_data_1 = pd.read_csv('data/daily_sales_data_1.csv')
daily_sales_data_2 = pd.read_csv('data/daily_sales_data_2.csv')

merged_df=pd.concat([daily_sales_data_0, daily_sales_data_1, daily_sales_data_2], ignore_index=True)
merged_df=merged_df[merged_df['product']=='pink morsel']

new_merged_df=merged_df.copy()
new_merged_df['price']=new_merged_df['price'].astype(str)
new_merged_df['price']=new_merged_df['price'].str.replace('$','')
new_merged_df['price']=new_merged_df['price'].astype(float)
new_merged_df['Sales']=new_merged_df['price']*new_merged_df['quantity']
daily_sales_data=new_merged_df.copy()
daily_sales_data.drop(columns=['product','price','quantity'], inplace=True)
print(daily_sales_data.head(5))


#task3
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Sales Data Visualization"),
    dcc.Graph(
        id='sales-graph',
        figure=px.line(daily_sales_data, x='date', y='Sales', title='Sales Over Time')
    )
])
if __name__ == '__main__':
    app.run(debug=True)