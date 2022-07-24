# -*- coding: utf-8 -*-
"""Pivot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TC99_A3O0AZGX-cS81KwLTeuiNos2lpc
"""

import pandas as pd
import numpy as np
import os

weather = pd.read_csv("weather_data.csv")
df = pd.DataFrame(weather)

df

df_pivot = df.pivot(index="DATE",columns='STATION', values = ["PRCP","TAVG","TMAX","TMIN"])

df_pivot

df_pivot.columns