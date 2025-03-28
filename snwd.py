def snwd_prep(df_25_SNWD, yesterday):
    print('snowd')
    df_25_SNWD["Daily Average"] = df_25_SNWD.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_SNWD_near = df_25_SNWD[['axisdate', 'Daily Average']]

    # make a df_go that drops duplicate values and is ready to graph
    df_25_SNWD_go = df_25_SNWD_near.drop_duplicates()

    # Waits a while before showing data to allow it time to update completely
    df_25_SNWD_go = df_25_SNWD_go[(df_25_SNWD_go["axisdate"]<=yesterday)]

    return df_25_SNWD_go

def snwd_decade(df_SNWD):
    print('yo momma')