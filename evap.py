import plotly.graph_objects as go

def evap_prep(df_25_EVAP, yesterday):
    
    df_25_EVAP["Daily Average"] = df_25_EVAP.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_EVAP_near = df_25_EVAP[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_25_EVAP_g = df_25_EVAP_near.drop_duplicates()

    # Waits a while before showing data to allow it time to update completely
    df_25_EVAP_g = df_25_EVAP_g[(df_25_EVAP_g["axisdate"]<=yesterday)]

    return df_25_EVAP_g

def evap_decade(df_EVAP):

    #take an the average of everything that has each month/day combo, make it a new column.
    df_EVAP["Daily Average"] = df_EVAP.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_EVAP_near = df_EVAP[['axisdate', 'Daily Average']]

    #drop every duplicate value, making a df_g that is ready to graph
    df_EVAP_g = df_EVAP_near.drop_duplicates()

    return df_EVAP_g

def fig_evap(df_25_EVAP_g, df_EVAP_g):
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
    return fig_EVAP