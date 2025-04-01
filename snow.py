import plotly.graph_objects as go

def snow_prep(df_25_SNOW, yesterday):
    
    df_25_SNOW["Daily Average"] = df_25_SNOW.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_SNOW_near = df_25_SNOW[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_25_SNOW_g = df_25_SNOW_near.drop_duplicates()

    # Waits a while before showing data to allow it time to update completely
    df_25_SNOW_g = df_25_SNOW_g[(df_25_SNOW_g["axisdate"]<=yesterday)]

    return df_25_SNOW_g

def snow_decade(df_SNOW):

    #take an the average of everything that has each month/day combo, make it a new column.
    df_SNOW["Daily Average"] = df_SNOW.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_SNOW_near = df_SNOW[['axisdate', 'Daily Average']]

    #drop every duplicate value, making a df_g that is ready to graph
    df_SNOW_g = df_SNOW_near.drop_duplicates()

    return df_SNOW_g

def fig_snow(df_25_SNOW_g, df_SNOW_g):
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
    return fig_SNOW