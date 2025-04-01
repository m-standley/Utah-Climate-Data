import plotly.graph_objects as go

def sn33_prep(df_25_SN33, df_25_SX33):
    print('made it to SN33_prep')

    #average same-day values
    df_25_SN33["Daily Average"] = df_25_SN33.groupby("axisdate")["value"].transform('mean')

    #average same-day values
    df_25_SX33["Daily Average"] = df_25_SX33.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_SN33_near = df_25_SN33[['axisdate', 'Daily Average']]

    #make a df that ignores every column except what you'll graph
    df_25_SX33_near = df_25_SX33[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_25_SN33_g = df_25_SN33_near.drop_duplicates()
    df_25_SN33_g['Daily Average'] = df_25_SN33_g['Daily Average']/10 #gets the units right. Now it's celsius

    # make a df_g that drops duplicate values and is ready to graph
    df_25_SX33_g = df_25_SX33_near.drop_duplicates()
    df_25_SX33_g['Daily Average'] = df_25_SX33_g['Daily Average']/10 # gets the units right. Now its celsius

    return df_25_SN33_g, df_25_SX33_g


def sn33_decade(df_SN33, df_SX33):
    print('made it to SN33_decade')
    #average same-day values
    df_SN33["Daily Average"] = df_SN33.groupby("date")["value"].transform('mean')

    #average same-day values
    df_SX33["Daily Average"] = df_SX33.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_SN33_near = df_SN33[['axisdate', 'Daily Average']]

    #make a df that ignores every column except what you'll graph
    df_SX33_near = df_SX33[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_SN33_g = df_SN33_near.drop_duplicates()
    df_SN33_g['Daily Average'] = df_SN33_g['Daily Average']/10 # fixes units into celsius

    # make a df_g that drops duplicate values and is ready to graph
    df_SX33_g = df_SX33_near.drop_duplicates()
    df_SX33_g['Daily Average'] = df_SX33_g['Daily Average']/10 # fixes units into celsius

    return df_SN33_g, df_SX33_g

def fig_sn33(df_SN33_g, df_SX33_g, df_25_SN33_g, df_25_SX33_g):
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
    return fig_SN33