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
from tmin import tmin_prep, tmin_decade
from evap import evap_prep, evap_decade
from snow import snow_prep, snow_decade
from wesd import wesd_prep, wesd_decade
from awnd import awnd_prep, awnd_decade
from sn33 import sn33_prep, sn33_decade
from wsfi import wsfi_prep, wsfi_decade
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
df_25_PRCP_g = prcp_prep(df_25_P, yesterday)
df_PRCP = df_all[df_all['element'] == 'PRCP']
df_PRCP_g = prcp_decade(df_PRCP)

# SNWD
df_25_SNWD = df[df['element'] == 'SNWD']
df_25_SNWD_g = snwd_prep(df_25_SNWD, yesterday)
df_SNWD = df_all[df_all['element'] == 'SNWD']
df_SNWD_g = snwd_decade(df_SNWD)

# TMIN/TMAX
df_25_TMIN = df[df['element'] == 'TMIN']
df_25_TMAX = df[df['element'] == 'TMAX']
df_25_TMIN_g = tmin_prep(df_25_TMIN, df_25_TMAX)
df_25_TMAX_g = tmin_prep(df_25_TMIN, df_25_TMAX)
df_TMIN = df_all[df_all['element'] == 'TMIN']
df_TMAX = df_all[df_all['element'] == 'TMAX']
df_TMIN_g = tmin_decade(df_TMIN)
df_TMAX_g = tmin_decade(df_TMAX)

# EVAP
df_25_EVAP = df[df['element'] == 'EVAP']
df_25_EVAP_g = evap_prep(df_25_EVAP, yesterday)
df_EVAP = df_all[df_all['element'] == 'EVAP']
df_EVAP_g = evap_decade(df_EVAP)

# SNOW
df_25_SNOW = df[df['element'] == 'SNOW']
df_25_SNOW_g = snow_prep(df_25_SNOW, yesterday)
df_SNOW = df_all[df_all['element'] == 'SNOW']
df_SNOW_g = snow_decade(df_SNOW)

# WESD
df_25_WESD = df[df['element'] == 'WESD']
df_25_WESD_g = wesd_prep(df_25_WESD, yesterday)
df_WESD = df_all[df_all['element'] == 'WESD']
df_WESD_g = wesd_decade(df_WESD)

# AWND
df_25_AWND = df[df['element'] == 'AWND']
df_25_AWND_g = awnd_prep(df_25_AWND, yesterday)
df_AWND = df_all[df_all['element'] == 'AWND']
df_AWND_g = awnd_decade(df_AWND)

# SN33/SX33
df_25_SN33 = df[df['element'] == 'SN33']
df_25_SX33 = df[df['element'] == 'SX33']
df_25_SN33_g = sn33_prep(df_25_SN33, df_25_SX33)
df_25_SX33_g = sn33_prep(df_25_SN33, df_25_SX33)
df_SN33 = df_all[df_all['element'] == 'SN33']
df_SX33 = df_all[df_all['element'] == 'SX33']
df_SN33_g = sn33_decade(df_SN33)
df_SX33_g = sn33_decade(df_SX33)

# WSFI
df_25_WSFI = df[df['element'] == 'WSFI']
df_25_WSFI_g = wsfi_prep(df_25_WSFI, yesterday)
df_WSFI = df_all[df_all['element'] == 'WSFI']
df_WSFI_g = wsfi_decade(df_WSFI)

dashboarder(df_25_PRCP_g, df_PRCP_g, df_25_SNWD_g, df_SNWD_g, df_25_TMIN_g, df_25_TMAX_g, df_TMIN_g, df_TMAX_g, df_25_EVAP_g, df_EVAP_g, df_25_SNOW_g, df_SNOW_g, df_25_WESD_g, df_WESD_g, df_25_AWND_g, df_AWND_g, df_25_SN33_g, df_25_SX33_g, df_SN33_g, df_SX33_g, df_25_WSFI_g, df_WSFI_g)


