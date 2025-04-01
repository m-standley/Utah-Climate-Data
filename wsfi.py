import plotly.graph_objects as go

def wsfi_prep(df_25_WSFI, yesterday):
    print('made it to WSFI_prep')
    df_25_WSFI["Daily Average"] = df_25_WSFI.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_WSFI_near = df_25_WSFI[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_25_WSFI_g = df_25_WSFI_near.drop_duplicates()

    # Waits a while before showing data to allow it time to update completely
    df_25_WSFI_g = df_25_WSFI_g[(df_25_WSFI_g["axisdate"]<=yesterday)]

    return df_25_WSFI_g

def wsfi_decade(df_WSFI):
    print('made it to WSFI_decade')
    #take an the average of everything that has each month/day combo, make it a new column.
    df_WSFI["Daily Average"] = df_WSFI.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_WSFI_near = df_WSFI[['axisdate', 'Daily Average']]

    #drop every duplicate value, making a df_g that is ready to graph
    df_WSFI_g = df_WSFI_near.drop_duplicates()

    return df_WSFI_g

def fig_wsfi(df_WSFI_g, df_25_WSFI_g):
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
    return fig_WSFI