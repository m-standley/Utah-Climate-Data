def wsfi_prep(df_25_WSFI, yesterday):
    print('made it to WSFI_prep')
    df_25_WSFI["Daily Average"] = df_25_WSFI.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_WSFI_near = df_25_WSFI[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_25_WSFI_g = df_25_WSFI_near.drop_duplicates()

    # Waits a while before showing data to allow it time to update completely
    df_25_WSFI_g = df_25_WSFI_g[(df_25_WSFI_g["axisdate"]<=yesterday)]

    return df_25_WSFI_g

def wsfi_decade(df_WSFI):
    print('made it to WSFI_decade')
    #take an the average of everything that has each month/day combo, make it a new column.
    df_WSFI["Daily Average"] = df_WSFI.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_WSFI_near = df_WSFI[['axisdate', 'Daily Average']]

    #drop every duplicate value, making a df_g that is ready to graph
    df_WSFI_g = df_WSFI_near.drop_duplicates()

    return df_WSFI_g