import plotly.graph_objects as go
import pandas as pd

def tmin_prep(df_25_TMIN, df_25_TMAX):
    print('made it to tmin_prep')

    # average same-day values
    df_25_TMIN["Daily Average"] = df_25_TMIN.groupby("axisdate")["value"].transform('mean')

    # average same-day values
    df_25_TMAX["Daily Average"] = df_25_TMAX.groupby("axisdate")["value"].transform('mean')

    # make a df that ignores every column except what you'll graph
    df_25_TMIN_near = df_25_TMIN[['axisdate', 'Daily Average']].copy() # Added .copy()
    df_25_TMAX_near = df_25_TMAX[['axisdate', 'Daily Average']].copy() # Added .copy()

    # make a df_g that drops duplicate values and is ready to graph
    df_25_TMIN_g = df_25_TMIN_near.drop_duplicates().copy() # Added .copy()
    df_25_TMIN_g.loc[:, 'Daily Average'] = df_25_TMIN_g['Daily Average'] / 10  # gets the units right. Now it's celsius

    # make a df_g that drops duplicate values and is ready to graph
    df_25_TMAX_g = df_25_TMAX_near.drop_duplicates().copy() # Added .copy()
    df_25_TMAX_g.loc[:, 'Daily Average'] = df_25_TMAX_g['Daily Average'] / 10  # gets the units right. Now its celsius

    return df_25_TMIN_g, df_25_TMAX_g



def tmin_decade(df_TMIN, df_TMAX):
    print('made it to tmin_decade')
    # average same-day values
    df_TMIN["Daily Average"] = df_TMIN.groupby("date")["value"].transform('mean')

    # average same-day values
    df_TMAX["Daily Average"] = df_TMAX.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_TMIN_near = df_TMIN[['axisdate', 'Daily Average']].copy() # Added .copy()

    #make a df that ignores every column except what you'll graph
    df_TMAX_near = df_TMAX[['axisdate', 'Daily Average']].copy() # Added .copy()

    # make a df_g that drops duplicate values and is ready to graph
    df_TMIN_g = df_TMIN_near.drop_duplicates().copy() # Added .copy()
    df_TMIN_g.loc[:, 'Daily Average'] = df_TMIN_g['Daily Average']/10 # fixes units into celsius

    # make a df_g that drops duplicate values and is ready to graph
    df_TMAX_g = df_TMAX_near.drop_duplicates().copy() # Added .copy()
    df_TMAX_g.loc[:, 'Daily Average'] = df_TMAX_g['Daily Average']/10 # fixes units into celsius

    return df_TMIN_g, df_TMAX_g



def fig_tmin(df_TMIN_g, df_TMAX_g, df_25_TMIN_g, df_25_TMAX_g):
    
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
    return fig_TMIN