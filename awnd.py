import plotly.graph_objects as go

def awnd_prep(df_25_AWND, yesterday):
    print('made it to AWND_prep')
    df_25_AWND["Daily Average"] = df_25_AWND.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_AWND_near = df_25_AWND[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_25_AWND_g = df_25_AWND_near.drop_duplicates()

    # Waits a while before showing data to allow it time to update completely
    df_25_AWND_g = df_25_AWND_g[(df_25_AWND_g["axisdate"]<=yesterday)]

    return df_25_AWND_g

def awnd_decade(df_AWND):
    print('made it to AWND_decade')
    #take an the average of everything that has each month/day combo, make it a new column.
    df_AWND["Daily Average"] = df_AWND.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_AWND_near = df_AWND[['axisdate', 'Daily Average']]

    #drop every duplicate value, making a df_g that is ready to graph
    df_AWND_g = df_AWND_near.drop_duplicates()

    return df_AWND_g

def fig_awnd(df_25_AWND_g, df_AWND_g):
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
    return fig_AWND