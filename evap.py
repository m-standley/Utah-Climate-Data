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