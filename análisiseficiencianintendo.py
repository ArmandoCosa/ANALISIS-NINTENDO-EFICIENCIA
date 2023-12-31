# -*- coding: utf-8 -*-
"""AnálisisEficienciaNintendo

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17QHZzZZ1QDUrXe6GfKAFr4B1vgwxAHxD

# `ANÁLISIS DE DATOS DE LOS RATIOS DE EFICIENCIA DE LA EMPRESA NINTENDO`

fuente: https://tools.morningstar.com.mx/mx/stockreport/default.aspx?tab=11&vw=er&SecurityToken=0P0001K4GZ%5D3%5D0%5DE0WWE%24%24ALL&Id=0P0001K4GZ&ClientFund=0&CurrencyId=MXN

LIBRERIAS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
import scipy.stats
from empiricaldist import Pmf, Cdf
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats as ss

!pip install empiricaldist

"""Cargar base de datos en CSV:"""

df= pd.read_csv("/content/AnalisisEficienciaNintendoCSV.csv")
df

"""# Colecta y validación de datos

¿Qué tipo de dato son las variables del conjunto de datos?
"""

(
df
.dtypes
.value_counts()
)

"""¿Cuántas variables de cada tipo de dato tenemos en el conjunto de datos?

"""

df.shape

"""¿Existen valores nulos explícitos en un conjunto de datos?"""

(
df
.isnull()
.any()
)

"""No existen valores nuelos en la database

# CONTEOS Y PROPORCIONES

Todas las variables
"""

df.describe(include= "all")

"""Categoricas

"""

df.describe(include=object)

sns.barplot(x = "2019", y = "DATO", data = df)

"""# MEDIDAS DE TENDENCIA CENTRAL"""

df.mean()

df.median()

df.mode()

"""# MEDIDAS DE DISPERCION"""

df.max()

df.min()

"""¿Cuál es el rango de las variables?"""

df.max(numeric_only=True)-df.min(numeric_only=True)

"""¿Cuál es la desviación estándar de las variables?

"""

df.std()

"""¿Cuál es el rango intercuartílico?"""

df.quantile()

"""# DISTRIBUCIONES

Funciones de probabilidad de masas del año 2019
"""

sns.histplot(
data=df,
x="2019",
binwidth=50,
stat="probability"
)

"""Funciones empíricas de probabilidad
acumulada del año 2019

"""

sns.ecdfplot(
data=df,
x="2019",
)

"""Comparando distribuciones del año 2019 con el 2020"""

sns.ecdfplot(
data=df,
x="2019",
hue="2020",
)

"""# FUNCIONES DE DENSIDAD DE
# PROBABILIDAD
"""

sns.kdeplot(
data=df,
x="2019",
)

"""# ANALISIS BIVARIADO

Estableciendo relaciones del año 2019 hasta el año 2023
"""

sns.displot(
data=df,
x="2019",
y="2020",
rug=True,
)

sns.displot(
data=df,
x="2019",
y="2021",
rug=True,
)

sns.displot(
data=df,
x="2019",
y="2022",
rug=True,
)

sns.displot(
data=df,
x="2019",
y="2023",
rug=True,
)

"""# ESTABLECIMIENTO DE RELACIONES

MATRICES DE CORRELACION

¿Existe una correlación lineal entre algunas de nuestras variables?
"""

df.corr()

sns.heatmap(
data=df.corr(),
cmap=sns.diverging_palette(20,230,as_cmap=True),
center=0,
vmin=0,
vmax=1,
linewidths=0.5,
annot=True,
)

"""# ANALISIS DE REGRESION SIMPLE

"""

sns.lmplot(
data=df,
x="2019",
y="2020",
height=10
)

sns.lmplot(
data=df,
x="2019",
y="2021",
height=10
)

sns.lmplot(
data=df,
x="2019",
y="2022",
height=10
)

sns.lmplot(
data=df,
x="2019",
y="2023",
height=10
)

"""# ANALISIS MULTIVARIADO

Modelo1
"""

model1= (
smf.ols(
data=df,
formula="Q('2019') ~ Q('2023')",
)
.fit()
)
model1.summary()

"""Modelo2"""

model2= (
smf.ols(
data=df,
formula="Q('2019') ~ Q('2023') + Q('2020')",
)
.fit()
)
model2.summary()

"""Modelo3"""

model3= (
smf.ols(
data=df,
formula="Q('2019') ~ Q('2023') + Q('2020') + Q('2021')",
)
.fit()
)
model3.summary()

"""Modelo4"""

model4= (
smf.ols(
data=df,
formula="Q('2019') ~ Q('2023') + Q('2020') + Q('2021') + Q('2022')",
)
.fit()
)
model4.summary()

modelos_resultados= pd.DataFrame(
dict(
actual_value=df["2019"],
prediction_model1= model1.predict(),
prediction_model2= model2.predict(),
prediction_model3= model3.predict(),
prediction_model4= model4.predict(),
)
)
modelos_resultados

"""ECDFs"""

sns.ecdfplot(
data=modelos_resultados
)

"""PDFs"""

sns.kdeplot(
data=modelos_resultados
)