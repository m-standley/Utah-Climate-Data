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