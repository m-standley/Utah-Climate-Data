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