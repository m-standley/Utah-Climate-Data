import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output

def dashboarder(df_25_PRCP_g, df_PRCP_g, df_25_SNWD_g, df_SNWD_g, df_25_TMIN_g, df_25_TMAX_g, df_TMIN_g, df_TMAX_g, df_25_EVAP_g, df_EVAP_g, df_25_SNOW_g, df_SNOW_g, df_25_WESD_g, df_WESD_g, df_25_AWND_g, df_AWND_g, df_25_SN33_g, df_25_SX33_g, df_SN33_g, df_SX33_g, df_25_WSFI_g, df_WSFI_g)
    print('made it to plots')

    #PRCP - Precipitation

    hue = 'steelblue' #line color of graph
    canvas = 'aliceblue' #background color
    reference = 'lightsteelblue' #color of reference line

    df_PRCP_g = df_PRCP_g.sort_values(by="axisdate")
    df_25_PRCP_g = df_25_PRCP_g.sort_values(by="axisdate")

    fig_PRCP = go.Figure ()
    fig_PRCP.add_trace(go.Scatter(x = df_PRCP_g["axisdate"],
                            y = df_PRCP_g["Daily Average"],
                            mode = "lines",
                            name = "Decade Average",
                            hoverinfo = 'none',
                            #connectgaps = False,
                            line = dict(color = reference,
                                        #shape = 'spline',
                                        width = 1)))
    fig_PRCP.add_trace(go.Scatter(x = df_25_PRCP_g["axisdate"],
                            y = df_25_PRCP_g["Daily Average"],
                            mode = "lines",
                            name = "2025",
                            connectgaps = True,
                            line = dict(color = hue,
                                        shape = 'spline',
                                        width = 3)))
    fig_PRCP.update_layout(plot_bgcolor = canvas,
                    paper_bgcolor = canvas,
                    legend_font_color = hue,
                    legend_orientation = 'h',
                    legend_yanchor = 'top',
                    legend_y = 1.15,
                    legend_xanchor = 'right',
                    legend_x = 1,
                    title = dict(text = "PRECIPITATION",
                                font_color = hue,
                                xanchor = 'left',
                                x = 0.074,
                                font_size = 25,
                                yanchor = 'top',
                                y = 0.84)
                                )
        
    fig_PRCP.update_xaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = False,
                    ticks = "inside",
                    ticklen = 5,
                    tickformat= "%b %d",
                    nticks = 12,
                    title = dict(text = ""),
                    )
    fig_PRCP.update_yaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = True,
                    ticks = 'inside',
                    ticklen = 5,
                    zeroline = False,
                    rangemode = 'tozero',
                    title = dict(text = "Precipitation (mm)")
                    )
    

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    # #SNWD - Snow Depth

    hue = 'slategrey' #line color of graph
    canvas = 'whitesmoke' #background color
    reference = 'silver' #color of reference line

    df_SNWD_g = df_SNWD_g.sort_values(by="axisdate")
    df_25_SNWD_g = df_25_SNWD_g.sort_values(by="axisdate")

    fig_SNWD = go.Figure ()
    fig_SNWD.add_trace(go.Scatter(x = df_SNWD_g["axisdate"],
                            y = df_SNWD_g["Daily Average"],
                            mode = "lines",
                            name = "Decade Average",
                            connectgaps = True,
                            hoverinfo = 'none',
                            line = dict(color = reference,
                                        shape = 'spline',
                                        width = 1)))
    fig_SNWD.add_trace(go.Scatter(x = df_25_SNWD_g["axisdate"],
                            y = df_25_SNWD_g["Daily Average"],
                            mode = "lines",
                            name = "2025",
                            connectgaps = True,
                            line = dict(color = hue,
                                        shape = 'spline',
                                        width = 3)))
    fig_SNWD.update_layout(plot_bgcolor = canvas,
                    paper_bgcolor = canvas,
                    legend_font_color = hue,
                    legend_orientation = 'h',
                    legend_yanchor = 'top',
                    legend_y = 1.15,
                    legend_xanchor = 'right',
                    legend_x = 1,
                    title = dict(text = "SNOW DEPTH",
                                font_color = hue,
                                xanchor = 'left',
                                x = 0.074,
                                font_size = 25,
                                yanchor = 'top',
                                y = 0.84)
                                )
        
    fig_SNWD.update_xaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = False,
                    ticks = "inside",
                    ticklen = 5,
                    tickformat= "%b %d",
                    nticks = 12,
                    title = dict(text = ""),
                    )
    fig_SNWD.update_yaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = True,
                    ticks = 'inside',
                    ticklen = 5,
                    zeroline = False,
                    rangemode = 'tozero',
                    title = dict(text = "Snow Depth (mm)")
                    )


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    # #TMIN / TMAX - Min and Max Temp

    hue = 'slategrey' #line color of graph
    canvas = 'whitesmoke' #background color
    referencemin = 'lightsteelblue' #color of reference line
    referencemax = 'salmon'
    mincolor = 'navy'
    maxcolor = 'firebrick'

    df_TMIN_g = df_TMIN_g.sort_values(by="axisdate")
    df_TMAX_g = df_TMAX_g.sort_values(by="axisdate")
    df_25_TMIN_g = df_25_TMIN_g.sort_values(by="axisdate")
    df_25_TMAX_g = df_25_TMAX_g.sort_values(by="axisdate")

    fig_TMIN = go.Figure ()
    fig_TMIN.add_trace(go.Scatter(x = df_TMIN_g["axisdate"],
                            y = df_TMIN_g["Daily Average"],
                            mode = "lines",
                            name = "Decade (Min)",
                            #connectgaps = False,
                            hoverinfo = 'none',
                            line = dict(color = referencemin,
                                        shape = 'spline',
                                        width = 1)))
    fig_TMIN.add_trace(go.Scatter(x = df_TMAX_g["axisdate"],
                            y = df_TMAX_g["Daily Average"],
                            mode = "lines",
                            name = "Decade (Max)",
                            #connectgaps = False,
                            hoverinfo = 'none',
                            line = dict(color = referencemax,
                                        shape = 'spline',
                                        width = 1)))
    fig_TMIN.add_trace(go.Scatter(x = df_25_TMIN_g["axisdate"],
                            y = df_25_TMIN_g["Daily Average"],
                            mode = "lines",
                            name = "2025 (Min)",
                            connectgaps = True,
                            line = dict(color = mincolor,
                                        shape = 'spline',
                                        width = 3)))
    fig_TMIN.add_trace(go.Scatter(x = df_25_TMAX_g["axisdate"],
                            y = df_25_TMAX_g["Daily Average"],
                            mode = "lines",
                            name = "2025 (Max)",
                            connectgaps = True,
                            line = dict(color = maxcolor,
                                        shape = 'spline',
                                        width = 3)))
    fig_TMIN.update_layout(plot_bgcolor = canvas,
                    paper_bgcolor = canvas,
                    legend_font_color = hue,
                    legend_orientation = 'v',
                    legend_yanchor = 'top',
                    legend_y = 1,
                    legend_xanchor = 'right',
                    legend_x = 1,
                    title = dict(text = "MAX / MIN TEMPERATURE",
                                font_color = hue,
                                xanchor = 'left',
                                x = 0.074,
                                font_size = 25,
                                yanchor = 'top',
                                y = 0.84)
                                )
        
    fig_TMIN.update_xaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = False,
                    ticks = "inside",
                    ticklen = 5,
                    tickformat= "%b %d",
                    nticks = 12,
                    title = dict(text = ""),
                    )
    fig_TMIN.update_yaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = True,
                    ticks = 'inside',
                    ticklen = 5,
                    zeroline = False,
                    rangemode = 'tozero',
                    title = dict(text = "Temperature (C)")
                    )
    

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    # #EVAP - EVAPORATION

    hue = 'teal' #line color of graph
    canvas = 'azure' #background color
    reference = 'lightblue' #color of reference line

    df_EVAP_g = df_EVAP_g.sort_values(by="axisdate")
    df_25_EVAP_g = df_25_EVAP_g.sort_values(by="axisdate")

    fig_EVAP = go.Figure ()
    fig_EVAP.add_trace(go.Scatter(x = df_EVAP_g["axisdate"],
                            y = df_EVAP_g["Daily Average"],
                            mode = "lines",
                            name = "Decade Average",
                            connectgaps = True,
                            hoverinfo = 'none',
                            line = dict(color = reference,
                                        shape = 'spline',
                                        width = 1)))
    fig_EVAP.add_trace(go.Scatter(x = df_25_EVAP_g["axisdate"],
                            y = df_25_EVAP_g["Daily Average"],
                            mode = "lines",
                            name = "2025",
                            connectgaps = True,
                            line = dict(color = hue,
                                        shape = 'spline',
                                        width = 3)))
    fig_EVAP.update_layout(plot_bgcolor = canvas,
                    paper_bgcolor = canvas,
                    showlegend = True,
                    legend_font_color = hue,
                    legend_orientation = 'h',
                    legend_yanchor = 'top',
                    legend_y = 1.15,
                    legend_xanchor = 'right',
                    legend_x = 1,
                    title = dict(text = "DAILY EVAPORATION",
                                font_color = hue,
                                xanchor = 'left',
                                x = 0.074,
                                font_size = 25,
                                yanchor = 'top',
                                y = 0.84)
                                )
        
    fig_EVAP.update_xaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = False,
                    ticks = "inside",
                    ticklen = 5,
                    tickformat= "%b %d",
                    nticks = 12,
                    range = ['2025-01-01', '2025-12-31'],
                    title = dict(text = ""),
                    )
    fig_EVAP.update_yaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = True,
                    ticks = 'inside',
                    ticklen = 5,
                    zeroline = False,
                    rangemode = 'tozero',
                    title = dict(text = "Evaporation (mm)")
                    )
    

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    #SNOW - SNOWFALL

    hue = 'darkslateblue' #line color of graph
    canvas = 'lavender' #background color
    reference = 'thistle' #color of reference line

    df_SNOW_g = df_SNOW_g.sort_values(by="axisdate")
    df_25_SNOW_g = df_25_SNOW_g.sort_values(by="axisdate")

    fig_SNOW = go.Figure ()
    fig_SNOW.add_trace(go.Scatter(x = df_SNOW_g["axisdate"],
                            y = df_SNOW_g["Daily Average"],
                            mode = "lines",
                            name = "Decade Average",
                            connectgaps = True,
                            hoverinfo = 'none',
                            line = dict(color = reference,
                                        shape = 'spline',
                                        width = 1)))
    fig_SNOW.add_trace(go.Scatter(x = df_25_SNOW_g["axisdate"],
                            y = df_25_SNOW_g["Daily Average"],
                            mode = "lines",
                            name = "2025",
                            connectgaps = True,
                            line = dict(color = hue,
                                        shape = 'spline',
                                        width = 3)))
    fig_SNOW.update_layout(plot_bgcolor = canvas,
                    paper_bgcolor = canvas,
                    showlegend = True,
                    legend_font_color = hue,
                    legend_orientation = 'h',
                    legend_yanchor = 'top',
                    legend_y = 1.15,
                    legend_xanchor = 'right',
                    legend_x = 1,
                    title = dict(text = "SNOWFALL",
                                font_color = hue,
                                xanchor = 'left',
                                x = 0.074,
                                font_size = 25,
                                yanchor = 'top',
                                y = 0.84)
                                )
        
    fig_SNOW.update_xaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = False,
                    ticks = "inside",
                    ticklen = 5,
                    tickformat= "%b %d",
                    nticks = 12,
                    range = ['2025-01-01', '2025-12-31'],
                    title = dict(text = ""),
                    )
    fig_SNOW.update_yaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = True,
                    ticks = 'inside',
                    ticklen = 5,
                    zeroline = False,
                    rangemode = 'tozero',
                    title = dict(text = "Snowfall (mm)")
                    )
    

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    #WESD - SNOW-WATER EQUIVALENT

    hue = 'steelblue' #line color of graph
    canvas = 'aliceblue' #background color
    reference = 'lightblue' #color of reference line

    df_WESD_g = df_WESD_g.sort_values(by="axisdate")
    df_25_WESD_g = df_25_WESD_g.sort_values(by="axisdate")

    fig_WESD = go.Figure ()
    fig_WESD.add_trace(go.Scatter(x = df_WESD_g["axisdate"],
                            y = df_WESD_g["Daily Average"],
                            mode = "lines",
                            name = "Decade Average",
                            connectgaps = True,
                            hoverinfo = 'none',
                            line = dict(color = reference,
                                        shape = 'spline',
                                        width = 1)))
    fig_WESD.add_trace(go.Scatter(x = df_25_WESD_g["axisdate"],
                            y = df_25_WESD_g["Daily Average"],
                            mode = "lines",
                            name = "2025",
                            connectgaps = True,
                            line = dict(color = hue,
                                        shape = 'spline',
                                        width = 3)))
    fig_WESD.update_layout(plot_bgcolor = canvas,
                    paper_bgcolor = canvas,
                    showlegend = True,
                    legend_font_color = hue,
                    legend_orientation = 'h',
                    legend_yanchor = 'top',
                    legend_y = 1.15,
                    legend_xanchor = 'right',
                    legend_x = 1,
                    title = dict(text = "SNOW WATER EQUIVALENT",
                                font_color = hue,
                                xanchor = 'left',
                                x = 0.074,
                                font_size = 25,
                                yanchor = 'top',
                                y = 0.84)
                                )
        
    fig_WESD.update_xaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = False,
                    ticks = "inside",
                    ticklen = 5,
                    tickformat= "%b %d",
                    nticks = 12,
                    range = ['2025-01-01', '2025-12-31'],
                    title = dict(text = ""),
                    )
    fig_WESD.update_yaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = True,
                    ticks = 'inside',
                    ticklen = 5,
                    zeroline = False,
                    rangemode = 'tozero',
                    title = dict(text = "Water Equivalent (mm)")
                    )
    

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    #AWND - AVERAGE DAILY WIND SPEED

    hue = 'darkgreen' #line color of graph
    canvas = 'honeydew' #background color
    reference = 'darkseagreen' #color of reference line

    df_AWND_g = df_AWND_g.sort_values(by="axisdate")
    df_25_AWND_g = df_25_AWND_g.sort_values(by="axisdate")

    fig_AWND = go.Figure ()
    fig_AWND.add_trace(go.Scatter(x = df_AWND_g["axisdate"],
                            y = df_AWND_g["Daily Average"],
                            mode = "lines",
                            name = "Decade Average",
                            connectgaps = True,
                            hoverinfo = 'none',
                            line = dict(color = reference,
                                        shape = 'spline',
                                        width = 1)))
    fig_AWND.add_trace(go.Scatter(x = df_25_AWND_g["axisdate"],
                            y = df_25_AWND_g["Daily Average"],
                            mode = "lines",
                            name = "2025",
                            connectgaps = True,
                            line = dict(color = hue,
                                        shape = 'spline',
                                        width = 3)))
    fig_AWND.update_layout(plot_bgcolor = canvas,
                    paper_bgcolor = canvas,
                    showlegend = True,
                    legend_font_color = hue,
                    legend_orientation = 'h',
                    legend_yanchor = 'top',
                    legend_y = 1.15,
                    legend_xanchor = 'right',
                    legend_x = 1,
                    title = dict(text = "AVERAGE DAILY WIND SPEED",
                                font_color = hue,
                                xanchor = 'left',
                                x = 0.074,
                                font_size = 25,
                                yanchor = 'top',
                                y = 0.84)
                                )
        
    fig_AWND.update_xaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = False,
                    ticks = "inside",
                    ticklen = 5,
                    tickformat= "%b %d",
                    nticks = 12,
                    range = ['2025-01-01', '2025-12-31'],
                    title = dict(text = ""),
                    )
    fig_AWND.update_yaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = True,
                    ticks = 'inside',
                    ticklen = 5,
                    zeroline = False,
                    rangemode = 'tozero',
                    title = dict(text = "Wind Speed (km/h)")
                    )
    
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    #SN33 / SX33 - Min and Max Soil Temp (Bare ground, depth of 20 cm)

    hue = 'slategrey' #line color of graph
    canvas = 'whitesmoke' #background color
    referencemin = 'lightsteelblue' #color of reference line
    referencemax = 'wheat'
    mincolor = 'navy'
    maxcolor = 'goldenrod'

    df_SN33_g = df_SN33_g.sort_values(by="axisdate")
    df_SX33_g = df_SX33_g.sort_values(by="axisdate")
    df_25_SN33_g = df_25_SN33_g.sort_values(by="axisdate")
    df_25_SX33_g = df_25_SX33_g.sort_values(by="axisdate")

    fig_SN33 = go.Figure ()
    fig_SN33.add_trace(go.Scatter(x = df_SN33_g["axisdate"],
                            y = df_SN33_g["Daily Average"],
                            mode = "lines",
                            name = "Decade (Min)",
                            #connectgaps = False,
                            hoverinfo = 'none',
                            line = dict(color = referencemin,
                                        shape = 'spline',
                                        width = 1)))
    fig_SN33.add_trace(go.Scatter(x = df_SX33_g["axisdate"],
                            y = df_SX33_g["Daily Average"],
                            mode = "lines",
                            name = "Decade (Max)",
                            #connectgaps = False,
                            hoverinfo = 'none',
                            line = dict(color = referencemax,
                                        shape = 'spline',
                                        width = 1)))
    fig_SN33.add_trace(go.Scatter(x = df_25_SN33_g["axisdate"],
                            y = df_25_SN33_g["Daily Average"],
                            mode = "lines",
                            name = "2025 (Min)",
                            connectgaps = True,
                            line = dict(color = mincolor,
                                        shape = 'spline',
                                        width = 3)))
    fig_SN33.add_trace(go.Scatter(x = df_25_SX33_g["axisdate"],
                            y = df_25_SX33_g["Daily Average"],
                            mode = "lines",
                            name = "2025 (Max)",
                            connectgaps = True,
                            line = dict(color = maxcolor,
                                        shape = 'spline',
                                        width = 3)))
    fig_SN33.update_layout(plot_bgcolor = canvas,
                    paper_bgcolor = canvas,
                    legend_font_color = hue,
                    legend_orientation = 'v',
                    legend_yanchor = 'top',
                    legend_y = 1,
                    legend_xanchor = 'right',
                    legend_x = 1,
                    title = dict(text = "MAX / MIN SOIL TEMPERATURE",
                                font_color = hue,
                                xanchor = 'left',
                                x = 0.074,
                                font_size = 25,
                                yanchor = 'top',
                                y = 0.84)
                                )
        
    fig_SN33.update_xaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = False,
                    ticks = "inside",
                    ticklen = 5,
                    tickformat= "%b %d",
                    nticks = 12,
                    title = dict(text = ""),
                    )
    fig_SN33.update_yaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = True,
                    ticks = 'inside',
                    ticklen = 5,
                    zeroline = False,
                    #rangemode = 'tozero',
                    title = dict(text = "Temperature (C)")
                    )
    
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    #WSFI - HIGHEST GUST SPEED

    hue = 'olive' #line color of graph
    canvas = 'ivory' #background color
    reference = 'darkkhaki' #color of reference line

    df_WSFI_g = df_WSFI_g.sort_values(by="axisdate")
    df_25_WSFI_g = df_25_WSFI_g.sort_values(by="axisdate")

    fig_WSFI = go.Figure ()
    fig_WSFI.add_trace(go.Scatter(x = df_WSFI_g["axisdate"],
                            y = df_WSFI_g["Daily Average"],
                            mode = "lines",
                            name = "Decade Average",
                            connectgaps = True,
                            hoverinfo = 'none',
                            line = dict(color = reference,
                                        shape = 'spline',
                                        width = 1)))
    fig_WSFI.add_trace(go.Scatter(x = df_25_WSFI_g["axisdate"],
                            y = df_25_WSFI_g["Daily Average"],
                            mode = "lines",
                            name = "2025",
                            connectgaps = True,
                            line = dict(color = hue,
                                        shape = 'spline',
                                        width = 3)))
    fig_WSFI.update_layout(plot_bgcolor = canvas,
                    paper_bgcolor = canvas,
                    showlegend = True,
                    legend_font_color = hue,
                    legend_orientation = 'h',
                    legend_yanchor = 'top',
                    legend_y = 1.15,
                    legend_xanchor = 'right',
                    legend_x = 1,
                    title = dict(text = "HIGHEST GUST SPEED",
                                font_color = hue,
                                xanchor = 'left',
                                x = 0.074,
                                font_size = 25,
                                yanchor = 'top',
                                y = 0.84)
                                )
        
    fig_WSFI.update_xaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = False,
                    ticks = "inside",
                    ticklen = 5,
                    tickformat= "%b %d",
                    nticks = 12,
                    range = ['2025-01-01', '2025-12-31'],
                    title = dict(text = ""),
                    )
    fig_WSFI.update_yaxes(color = hue,
                    gridcolor = hue,
                    linecolor = hue,
                    mirror = True,
                    showgrid = True,
                    ticks = 'inside',
                    ticklen = 5,
                    zeroline = False,
                    rangemode = 'tozero',
                    title = dict(text = "Wind Speed (km/h)")
                    )
    

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    # Dashboard

    all_viz = ["fig_PRCP", "fig_SNOW", "fig_SNWD", "fig_WESD", "fig_EVAP", "fig_TMIN", "fig_SN33", "fig_AWND", "fig_WSFI"]

    graph1 = fig_PRCP
    graph2 = fig_SNOW
    graph3 = fig_SNWD
    graph4 = fig_WESD
    graph5 = fig_EVAP
    graph6 = fig_TMIN
    graph7 = fig_SN33
    graph8 = fig_AWND
    graph9 = fig_WSFI

    app = dash.Dash(__name__)

    app.layout = html.Div(
        id='app-container',
        style={'padding': '20px'},
        children=[
            html.H1(
                "UTAH WEATHER AND CLIMATE",
                id='title-text',
                style={
                    'fontFamily': 'Arial, sans-serif',
                    'fontSize': '36px',
                    'textAlign': 'center',
                    'marginBottom': '20px'
                }
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
                        {'label': 'Wind Speed', 'value': 'graph8'},
                        {'label': 'Wind Gusts', 'value': 'graph9'}
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
        title_style = {'fontFamily': 'Arial', 'fontSize': '30px','textAlign': 'center', 'marginBottom': '10px'} #create title style.

        if selected_graph == 'graph1':
            textcolor = 'rgb(241,248,254)'
            color = 'rgb(85,129,176)'
            dropdown_style['backgroundColor'] = textcolor
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(220,235,250)'
            title_style['color'] = color #set title color
            return graph1, "This is a measure, in millimeters, of how much water (both rain and snow) has fallen in the last 24 hours. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style

        elif selected_graph == 'graph2':
            textcolor = 'rgb(230,220,248)'
            color = 'rgb(70,61,134)'
            dropdown_style['backgroundColor'] = textcolor
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(215,210,240)'
            title_style['color'] = color
            return graph2, "This is a measure, in millimeters,  of how much snow has fallen in the last 24 hours. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style

        elif selected_graph == 'graph3':
            textcolor = 'rgb(245,245,245)'
            color = 'rgb(115,127,142)'
            dropdown_style['backgroundColor'] = textcolor
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(235,235,235)'
            title_style['color'] = color
            return graph3, "This is a measure of how deep the snow is, in millimeters. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style

        elif selected_graph == 'graph4':
            textcolor = 'rgb(241,248,254)'
            color = 'rgb(85,129,176)'
            dropdown_style['backgroundColor'] = textcolor
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(220,235,250)'
            title_style['color'] = color
            return graph4, "Snow water equivalent (SWE) is a measure of how much water would be produced if the snow were to melt, here recorded in millimeters. A higher SWE means a heavier, wetter snow. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style

        elif selected_graph == 'graph5':
            textcolor = 'rgb(243,255,255)'
            color = 'rgb(55,126,127)'
            dropdown_style['backgroundColor'] = textcolor
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(220,240,240)'
            title_style['color'] = color
            return graph5, "This is a measure, in millimeters, of how much water is lost due to natural evaporation over the course of 24 hours. Evaporation is measured by placing a pan of water in a sunny area and measuring how much is lost over time. In the environment, water loss due to evaporation can take place in water bodies, the soil, and even plants. Evaporation can be very rapid under hot and dry conditions. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style

        elif selected_graph == 'graph6':
            textcolor = 'rgb(245,245,245)'
            color = 'rgb(115,127,142)'
            dropdown_style['backgroundColor'] = textcolor
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(235,235,235)'
            title_style['color'] = color
            return graph6, "This is a measure, in Celsius, of the maximum and minimum daily air temperatures. These measurements represent daily averages for the entire state.", explanation_style, dropdown_style, app_style, title_style

        elif selected_graph == 'graph7':
            textcolor = 'rgb(245,245,245)'
            color = 'rgb(115,127,142)'
            dropdown_style['backgroundColor'] = textcolor
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(235,235,235)'
            title_style['color'] = color
            return graph7, "This is a measure, in Celsius, of the maximum and minimum daily soil temperatures. Measurements were taken on bare soil at a depth of 20 cm. These measurements represent daily averages for the entire state.", explanation_style, dropdown_style, app_style, title_style

        elif selected_graph == 'graph8':
            textcolor = 'rgb(243,255,241)'
            color = 'rgb(41,98,24)'
            dropdown_style['backgroundColor'] = textcolor
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(220,240,220)'
            title_style['color'] = color
            return graph8, "This is a measure, in kilometers per hour, of the average daily wind speed. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style

        elif selected_graph == 'graph9':
            textcolor = 'rgb(255,255,241)'
            color = 'rgb(128,128,38)'
            dropdown_style['backgroundColor'] = textcolor
            dropdown_style['color'] = color
            explanation_style['color'] = color
            app_style['backgroundColor'] = 'rgb(240,240,220)'
            title_style['color'] = color
            return graph9, "This is a measure, in kilometers per hour, of the maximum daily wind speed. Individual wind gusts can be considerably faster and more destructive than the average daily wind speed. This measurement represents a daily average of maximum gust speed for the entire state.", explanation_style, dropdown_style, app_style, title_style

        else:
            dropdown_style['backgroundColor'] = 'white'
            dropdown_style['color'] = 'black'
            explanation_style['color'] = 'black'
            app_style['backgroundColor'] = 'rgb(240,240,240)'
            title_style['color'] = 'black'
            return {}, "", explanation_style, dropdown_style, app_style, title_style

    if __name__ == '__main__':
        app.run(debug=True)

    return app