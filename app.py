from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("pink_morsel_sales.csv")
fig = px.line(df, x="date", y="sales", color="region")

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Graph',
            style={
            'textAlign': 'center'
            }
        ),
    html.Div(children=
            'From the data, it can be concluded that the sales are higher after the price increase on the 15th of January, 2021',    
            style={'textAlign': 'center'
            }  
        ),

    dcc.Graph(
        id='Sales Graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)