def tmin_prep(df_25_TMIN, df_25_TMAX):
    print('made it to tmin_prep')

    #average same-day values
    df_25_TMIN["Daily Average"] = df_25_TMIN.groupby("axisdate")["value"].transform('mean')

    #average same-day values
    df_25_TMAX["Daily Average"] = df_25_TMAX.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_TMIN_near = df_25_TMIN[['axisdate', 'Daily Average']]

    #make a df that ignores every column except what you'll graph
    df_25_TMAX_near = df_25_TMAX[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_25_TMIN_g = df_25_TMIN_near.drop_duplicates()
    df_25_TMIN_g['Daily Average'] = df_25_TMIN_g['Daily Average']/10 #gets the units right. Now it's celsius

    # make a df_g that drops duplicate values and is ready to graph
    df_25_TMAX_g = df_25_TMAX_near.drop_duplicates()
    df_25_TMAX_g['Daily Average'] = df_25_TMAX_g['Daily Average']/10 # gets the units right. Now its celsius

    return df_25_TMIN_g, df_25_TMAX_g


def tmin_decade(df_TMIN, df_TMAX):
    print('made it to tmin_decade')
    #average same-day values
    df_TMIN["Daily Average"] = df_TMIN.groupby("date")["value"].transform('mean')

    #average same-day values
    df_TMAX["Daily Average"] = df_TMAX.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_TMIN_near = df_TMIN[['axisdate', 'Daily Average']]

    #make a df that ignores every column except what you'll graph
    df_TMAX_near = df_TMAX[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_TMIN_g = df_TMIN_near.drop_duplicates()
    df_TMIN_g['Daily Average'] = df_TMIN_g['Daily Average']/10 # fixes units into celsius

    # make a df_g that drops duplicate values and is ready to graph
    df_TMAX_g = df_TMAX_near.drop_duplicates()
    df_TMAX_g['Daily Average'] = df_TMAX_g['Daily Average']/10 # fixes units into celsius

    return df_TMIN_g, df_TMAX_g