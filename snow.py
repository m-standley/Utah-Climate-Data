def snow_prep(df_25_SNOW, yesterday):
    
    df_25_SNOW["Daily Average"] = df_25_SNOW.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_SNOW_near = df_25_SNOW[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_25_SNOW_g = df_25_SNOW_near.drop_duplicates()

    # Waits a while before showing data to allow it time to update completely
    df_25_SNOW_g = df_25_SNOW_g[(df_25_SNOW_g["axisdate"]<=yesterday)]

    return df_25_SNOW_g

def snow_decade(df_SNOW):

    #take an the average of everything that has each month/day combo, make it a new column.
    df_SNOW["Daily Average"] = df_SNOW.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_SNOW_near = df_SNOW[['axisdate', 'Daily Average']]

    #drop every duplicate value, making a df_g that is ready to graph
    df_SNOW_g = df_SNOW_near.drop_duplicates()

    return df_SNOW_g