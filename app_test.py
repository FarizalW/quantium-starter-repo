import pytest
import pandas as pd
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px

# Create a test fixture to provide the app instance
@pytest.fixture
def get_app():
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
            style={'textAlign': 'center'}
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
                          color="region")
        else:
            fig = px.line(filtered_df, x="date", y="sales",
                          hover_name="region")

        fig.update_layout(transition_duration=500)

        return fig

    return app

# Test for the update_figure callback function
def test_update_figure(get_app):
    app = get_app()

    # Test for 'all' region
    selected_region = "all"
    figure = app.update_figure(selected_region)
    assert len(figure.data) == 5  # Check for 5 data lines (one for each region)

    # Test for specific region
    selected_region = "north"
    figure = app.update_figure(selected_region)
    assert len(figure.data) == 1  # Check for 1 data line (for selected region)

    # Test for hover tool
    assert figure.data[0].hover_name == "region"  # Check for hover_name set to 'region'