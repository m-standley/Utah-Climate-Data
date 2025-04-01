def snwd_prep(df_25_SNWD, yesterday):
    
    df_25_SNWD["Daily Average"] = df_25_SNWD.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_SNWD_near = df_25_SNWD[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_25_SNWD_g = df_25_SNWD_near.drop_duplicates()

    # Waits a while before showing data to allow it time to update completely
    df_25_SNWD_g = df_25_SNWD_g[(df_25_SNWD_g["axisdate"]<=yesterday)]

    return df_25_SNWD_g

def snwd_decade(df_SNWD):
    
    df_SNWD = df_SNWD.sort_values(by='axisdate')  

    #take an the average of everything that has each month/day combo, make it a new column.
    df_SNWD["Daily Average"] = df_SNWD.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_SNWD_near = df_SNWD[['axisdate', 'Daily Average']]

    #drop every duplicate value, making a df_g that is ready to graph
    df_SNWD_g = df_SNWD_near.drop_duplicates()

    return df_SNWD_g