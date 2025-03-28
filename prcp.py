def prcp_prep(df_25_P, yesterday):
    print('made it to prcp_prep')

    df_25_P["Daily Average"] = df_25_P.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_P_near = df_25_P[['axisdate', 'Daily Average']]
    # make a df_go that drops duplicate values and is ready to graph
    df_25_PRCP_go = df_25_P_near.drop_duplicates()
    df_25_PRCP_go = df_25_PRCP_go[(df_25_PRCP_go["axisdate"]<=yesterday)]

    return df_25_PRCP_go

def prcp_decade(df_PRCP):
    print('yo momma')
    df_PRCP = df_PRCP.sort_values(by='axisdate')
    #take an the average of everything that has each month/day combo, make it a new column.
    df_PRCP["Daily Average"] = df_PRCP.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_PRCP_near = df_PRCP[['axisdate', 'Daily Average']]

    #drop every duplicate value, making a df_go that is ready to graph
    df_PRCP_go = df_PRCP_near.drop_duplicates()

    return df_PRCP_go