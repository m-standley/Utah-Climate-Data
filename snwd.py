import plotly.graph_objects as go

def snwd_prep(df_25_SNWD, yesterday):
    
    df_25_SNWD["Daily Average"] = df_25_SNWD.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_SNWD_near = df_25_SNWD[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_25_SNWD_g = df_25_SNWD_near.drop_duplicates()

    # Waits a while before showing data to allow it time to update completely
    df_25_SNWD_g = df_25_SNWD_g[(df_25_SNWD_g["axisdate"]<=yesterday)]

    return df_25_SNWD_g

def snwd_decade(df_SNWD):
    
    df_SNWD = df_SNWD.sort_values(by='axisdate')  

    #take an the average of everything that has each month/day combo, make it a new column.
    df_SNWD["Daily Average"] = df_SNWD.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_SNWD_near = df_SNWD[['axisdate', 'Daily Average']]

    #drop every duplicate value, making a df_g that is ready to graph
    df_SNWD_g = df_SNWD_near.drop_duplicates()

    return df_SNWD_g

def fig_snwd(df_25_SNWD_g, df_SNWD_g):
     
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
    return fig_SNWD