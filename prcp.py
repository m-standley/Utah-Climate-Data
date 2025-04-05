import plotly.graph_objects as go

def prcp_prep(df_25_P, yesterday):
    print('made it to prcp_prep')

    df_25_P["Daily Average"] = df_25_P.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_P_near = df_25_P[['axisdate', 'Daily Average']]
    # make a df_g that drops duplicate values and is ready to graph
    df_25_PRCP_g = df_25_P_near.drop_duplicates()
    df_25_PRCP_g = df_25_PRCP_g[(df_25_PRCP_g["axisdate"]<=yesterday)]

    return df_25_PRCP_g

def prcp_decade(df_PRCP):
    print('made it to PRCP_decade')
    df_PRCP = df_PRCP.sort_values(by='axisdate')
    #take an the average of everything that has each month/day combo, make it a new column.
    df_PRCP["Daily Average"] = df_PRCP.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_PRCP_near = df_PRCP[['axisdate', 'Daily Average']]

    #drop every duplicate value, making a df_g that is ready to graph
    df_PRCP_g = df_PRCP_near.drop_duplicates()

    return df_PRCP_g

def fig_prcp(df_PRCP_g, df_25_PRCP_g):
    

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
    return fig_PRCP
    