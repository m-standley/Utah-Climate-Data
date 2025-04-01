import plotly.graph_objects as go

def wesd_prep(df_25_WESD, yesterday):
    print('made it to wesd_prep')
    df_25_WESD["Daily Average"] = df_25_WESD.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_WESD_near = df_25_WESD[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_25_WESD_g = df_25_WESD_near.drop_duplicates()

    # Waits a while before showing data to allow it time to update completely
    df_25_WESD_g = df_25_WESD_g[(df_25_WESD_g["axisdate"]<=yesterday)]

    return df_25_WESD_g

def wesd_decade(df_WESD):
    print('made it to wesd_decade')
    #take an the average of everything that has each month/day combo, make it a new column.
    df_WESD["Daily Average"] = df_WESD.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_WESD_near = df_WESD[['axisdate', 'Daily Average']]

    #drop every duplicate value, making a df_g that is ready to graph
    df_WESD_g = df_WESD_near.drop_duplicates()

    return df_WESD_g

def fig_wesd(df_25_WESD_g, df_WESD_g):
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
    return fig_WESD