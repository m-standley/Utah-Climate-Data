import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output

def dashboarder(fig_PRCP, fig_SNWD, fig_TMIN, fig_EVAP, fig_SNOW, fig_WESD, fig_AWND, fig_SN33):
    print('made it to dashboard')

    # Dashboard

    all_viz = ["fig_PRCP", "fig_SNOW", "fig_SNWD", "fig_WESD", "fig_EVAP", "fig_TMIN", "fig_SN33", "fig_AWND"]

    graph1 = fig_PRCP
    graph2 = fig_SNOW
    graph3 = fig_SNWD
    graph4 = fig_WESD
    graph5 = fig_EVAP
    graph6 = fig_TMIN
    graph7 = fig_SN33
    graph8 = fig_AWND

    app = dash.Dash(__name__)

    app.layout = html.Div(
        id='app-container',
        style={'padding': '20px'},
        children=[
            html.Div(  # Container for the main title and subtitle
                style={'textAlign': 'center', 'marginBottom': '20px'},
                children=[
                    html.H1(
                        "UTAH WEATHER AND CLIMATE",
                        id='title-text',
                        style={
                            'fontFamily': 'Arial, sans-serif',
                            'fontSize': '36px',
                            'marginBottom': '5px'
                        }
                    ),
                    html.H3(  # Subtitle
                        "Using Data From NOAA's Global Historical Climatology Network",
                        id='subtitle-text',
                        style={
                            'fontFamily': 'Arial, sans-serif',
                            'fontSize': '12px',
                            'textAlign': 'center',
                            'marginTop': '0px'
                        }
                    ),
                ]
            ),
            dcc.Dropdown(
                id='graph-selector',
                options=[{'label': 'Precipitation', 'value': 'graph1'},
                        {'label': 'Snowfall', 'value': 'graph2'},
                        {'label': 'Snow Depth', 'value': 'graph3'},
                        {'label': 'Snow Water Equivalent', 'value': 'graph4'},
                        {'label': 'Evaporation', 'value': 'graph5'},
                        {'label': 'Temperature', 'value': 'graph6'},
                        {'label': 'Soil Temperature', 'value': 'graph7'},
                        {'label': 'Wind Speed', 'value': 'graph8'}
                        ],
                value='graph1',
                style={
                    'width': '200px',
                    'backgroundColor': '#f0f0f0',
                    'border': '1px solid #aaa',
                    'fontFamily': 'Arial, sans-serif',
                    'fontSize': '14px',
                    'fontWeight': 'normal'
                },
                className='custom-dropdown'
            ),
            dcc.Graph(id='selected-graph'),
            html.Div(id='graph-explanation', style={'marginTop': '30px',
                                                    'marginBottom': '30px',
                                                    'fontFamily': 'Arial, sans-serif',
                                                    'fontSize': '16px', })
        ]
    )


    @app.callback(
        Output('selected-graph', 'figure'),
        Output('graph-explanation', 'children'),
        Output('graph-explanation', 'style'),
        Output('graph-selector', 'style'),
        Output('app-container', 'style'),
        Output('title-text', 'style'),
        Output('subtitle-text', 'style'),
        Input('graph-selector', 'value')
    )
    def update_graph(selected_graph):
        dropdown_style = {
            'width': '200px',
            'fontFamily': 'Arial, sans-serif',
            'fontSize': '14px'
        }
        explanation_style = {'fontFamily': 'Arial, sans-serif', 'marginTop': '30px','marginBottom': '30px'}
        app_style = {'padding': '20px'}
        title_style = {'fontFamily': 'Arial', 'fontSize': '30px','textAlign': 'center', 'marginBottom': '5px'}
        subtitle_style = {'fontFamily': 'Arial, sans-serif', 'fontSize': '12px', 'textAlign': 'center', 'marginTop': '0px'}

        if selected_graph == 'graph1':
            color = 'rgb(85,129,176)'
            dropdown_style['backgroundColor'] = 'rgb(241,248,254)'
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(220,235,250)'
            title_style['color'] = color
            subtitle_style['color'] = color
            return graph1, "This is a measure, in millimeters, of how much water (both rain and snow) has fallen in the last 24 hours. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style, subtitle_style

        elif selected_graph == 'graph2':
            color = 'rgb(70,61,134)'
            dropdown_style['backgroundColor'] = 'rgb(230,220,248)'
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(215,210,240)'
            title_style['color'] = color
            subtitle_style['color'] = color
            return graph2, "This is a measure, in millimeters,  of how much snow has fallen in the last 24 hours. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style, subtitle_style

        elif selected_graph == 'graph3':
            color = 'rgb(115,127,142)'
            dropdown_style['backgroundColor'] = 'rgb(245,245,245)'
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(235,235,235)'
            title_style['color'] = color
            subtitle_style['color'] = color
            return graph3, "This is a measure of how deep the snow is, in millimeters. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style, subtitle_style

        elif selected_graph == 'graph4':
            color = 'rgb(85,129,176)'
            dropdown_style['backgroundColor'] = 'rgb(241,248,254)'
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(220,235,250)'
            title_style['color'] = color
            subtitle_style['color'] = color
            return graph4, "Snow water equivalent (SWE) is a measure of how much water would be produced if the snow were to melt, here recorded in millimeters. A higher SWE means a heavier, wetter snow. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style, subtitle_style

        elif selected_graph == 'graph5':
            color = 'rgb(55,126,127)'
            dropdown_style['backgroundColor'] = 'rgb(243,255,255)'
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(220,240,240)'
            title_style['color'] = color
            subtitle_style['color'] = color
            return graph5, "This is a measure, in millimeters, of how much water is lost due to natural evaporation over the course of 24 hours. Evaporation is measured by placing a pan of water in a sunny area and measuring how much is lost over time. In the environment, water loss due to evaporation can take place in water bodies, the soil, and even plants. Evaporation can be very rapid under hot and dry conditions. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style, subtitle_style

        elif selected_graph == 'graph6':
            color = 'rgb(115,127,142)'
            dropdown_style['backgroundColor'] = 'rgb(245,245,245)'
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(235,235,235)'
            title_style['color'] = color
            subtitle_style['color'] = color
            return graph6, "This is a measure, in Celsius, of the maximum and minimum daily air temperatures. These measurements represent daily averages for the entire state.", explanation_style, dropdown_style, app_style, title_style, subtitle_style

        elif selected_graph == 'graph7':
            color = 'rgb(115,127,142)'
            dropdown_style['backgroundColor'] = 'rgb(245,245,245)'
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(235,235,235)'
            title_style['color'] = color
            subtitle_style['color'] = color
            return graph7, "This is a measure, in Celsius, of the maximum and minimum daily soil temperatures. Measurements were taken on bare soil at a depth of 20 cm. These measurements represent daily averages for the entire state.", explanation_style, dropdown_style, app_style, title_style, subtitle_style

        elif selected_graph == 'graph8':
            color = 'rgb(41,98,24)'
            dropdown_style['backgroundColor'] = 'rgb(243,255,241)'
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(220,240,220)'
            title_style['color'] = color
            subtitle_style['color'] = color
            return graph8, "This is a measure, in kilometers per hour, of the average daily wind speed. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style, subtitle_style

        else:
            color = 'black'
            dropdown_style['backgroundColor'] = 'white'
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(240,240,240)'
            title_style['color'] = color
            subtitle_style['color'] = color
            return {}, "", explanation_style, dropdown_style, app_style, title_style, subtitle_style


    app.run(debug=True)