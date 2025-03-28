from google.cloud import bigquery
import os
import pandas as pd
from datetime import datetime, timedelta
import plotly.io as pio
import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from prcp import prcp_prep, prcp_decade
from snwd import snwd_prep, snwd_decade
from dashboarder import dashboarder


os.environ["GCLOUD_PROJECT"] = "climate-data-452305"
client = bigquery.Client()
pio.renderers.default = "plotly_mimetype"

with open('select_statement.sql', 'r') as sql_file:
    sql = sql_file.read()

# Read in data used for all visualisations
df = client.query_and_wait(sql).to_dataframe()

# Modify copies without modifying df and causing an error
pd.options.mode.copy_on_write = True

# convert string 'date' to datetime 'date_converted'
df['date_converted'] = pd.to_datetime(df['date'], format = '%Y-%m-%d')

# convert datetime 'date_converted' into 'axisdate' and normalized the year
df['axisdate'] = pd.to_datetime(df['date_convderted'].dt.strftime('2025-%m-%d'),format = '%Y-%m-%d', errors="coerce")

# filters out leap year
df = df[df.axisdate.notnull()]

yesterday = datetime.now() - timedelta(days = 4)

# read in decade data
df_all = pd.read_csv('df_all.csv', sep=",")

# PRCP
df_25_P = df[df['element'] == 'PRCP']
df_25_PRCP_go = prcp_prep(df_25_P, yesterday)
df_PRCP = df_all[df_all['element'] == 'PRCP']
df_PRCP_go = prcp_decade(df_PRCP)

# SNWD
df_25_SNWD = df[df['element'] == 'SNWD']
df_25_SNWD_go = snwd_prep(df_25_SNWD, yesterday)



dashboarder(df_25_PRCP_go, df_PRCP_go)


