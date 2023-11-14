from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("pink_morsel_sales.csv")
df = df.sort_values(by='date')

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Graph',
            style={
            'textAlign': 'center',
            'background-color' : '#D598EB'
            }
        ),
    html.Div(children=
            'From the data, it can be concluded that the sales are higher after the price increase on the 15th of January, 2021',    
            style={'textAlign': 'center'
            }  
        ),
     dcc.RadioItems(
            options=["north", "east", "south", "west", "all"],
            value="north",
            id="region_picker",
            inline=True
        ),
    dcc.Graph(
        id='sales_graph',
    )
])

@callback(
    Output('sales_graph', 'figure'),
    Input('region_picker', 'value'))

def update_figure(selected_region):
    filtered_df = df[df.region == selected_region]
    if selected_region == "all":
        fig = px.line(df, x="date", y="sales",
                     color="region",
                     )
    else:
        fig = px.line(filtered_df, x="date", y="sales",
                     hover_name="region",
                     )
    

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run(debug=True)