def sn33_prep(df_25_SN33, df_25_SX33):
    print('made it to SN33_prep')

    #average same-day values
    df_25_SN33["Daily Average"] = df_25_SN33.groupby("axisdate")["value"].transform('mean')

    #average same-day values
    df_25_SX33["Daily Average"] = df_25_SX33.groupby("axisdate")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_25_SN33_near = df_25_SN33[['axisdate', 'Daily Average']]

    #make a df that ignores every column except what you'll graph
    df_25_SX33_near = df_25_SX33[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_25_SN33_g = df_25_SN33_near.drop_duplicates()
    df_25_SN33_g['Daily Average'] = df_25_SN33_g['Daily Average']/10 #gets the units right. Now it's celsius

    # make a df_g that drops duplicate values and is ready to graph
    df_25_SX33_g = df_25_SX33_near.drop_duplicates()
    df_25_SX33_g['Daily Average'] = df_25_SX33_g['Daily Average']/10 # gets the units right. Now its celsius

    return df_25_SN33_g, df_25_SX33_g


def sn33_decade(df_SN33, df_SX33):
    print('made it to SN33_decade')
    #average same-day values
    df_SN33["Daily Average"] = df_SN33.groupby("date")["value"].transform('mean')

    #average same-day values
    df_SX33["Daily Average"] = df_SX33.groupby("date")["value"].transform('mean')

    #make a df that ignores every column except what you'll graph
    df_SN33_near = df_SN33[['axisdate', 'Daily Average']]

    #make a df that ignores every column except what you'll graph
    df_SX33_near = df_SX33[['axisdate', 'Daily Average']]

    # make a df_g that drops duplicate values and is ready to graph
    df_SN33_g = df_SN33_near.drop_duplicates()
    df_SN33_g['Daily Average'] = df_SN33_g['Daily Average']/10 # fixes units into celsius

    # make a df_g that drops duplicate values and is ready to graph
    df_SX33_g = df_SX33_near.drop_duplicates()
    df_SX33_g['Daily Average'] = df_SX33_g['Daily Average']/10 # fixes units into celsius

    return df_SN33_g, df_SX33_g