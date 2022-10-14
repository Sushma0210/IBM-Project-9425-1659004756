# -*- coding: utf-8 -*-
"""Revathi_Assignment_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Osm9drf1ug4R6VuvIeVWrkHTgRxBurLd
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""#Load the dataset"""

ds=pd.read_csv("Churn_Modelling.csv")
ds

ds.describe()

ds.head()

"""#VISUALIZATION

*   Univariate Analysis
"""

sns.distplot(ds['CreditScore'],bins=15,kde=False)

sns.distplot(ds['Tenure'],bins=30,hist=False)

"""

*   Bi - Variate Analysis

"""

sns.relplot(x="CreditScore",y='EstimatedSalary',data=ds)

sns.relplot(x="Tenure",y='Exited',data=ds)

sns.catplot(x ="HasCrCard",y='IsActiveMember',order=['No','Yes'],data=ds)

"""

*   Multi - Variate Analysis


"""

sns.boxplot(x ='CreditScore',y='EstimatedSalary',data=ds)

""" **descriptive statistics on the dataset.**

"""

df = pd.DataFrame(ds)
df

"""# Handle the Missing values.

"""

df['CreditScore'].mean()

df['CreditScore'].fillna(df['CreditScore'].mean(),inplace=True)

df['Balance'].fillna(df['Balance'].mean(),inplace=True)

df['Geography'].mode()[0]

df['Geography'].fillna(df['Geography'].mode()[0],inplace=True)

df.isnull().any()

"""# Find the outliers and replace the outliers"""

url = 'https://drive.google.com/file/d/14pTYMZnpAihmWNSlBV0ArGEqSPP3xdnJ/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
dataset = pd.read_csv("Churn_Modelling.csv")

dataset

dataset.isnull().any()

dataset.describe()

dataset.skew()

sns.boxplot(dataset["EstimatedSalary"])

sns.kdeplot(dataset["EstimatedSalary"])

sns.boxplot(dataset["HasCrCard"])

sns.kdeplot(dataset["CustomerId"])

q1 = dataset["CreditScore"].describe()["25%"]

q1

q3 = dataset["CreditScore"].describe()["75%"]

q3

iqr = q3-q1  # iqr

l_b = q1 -(1.5*iqr)
u_b = q3 + (1.5*iqr)

l_b

u_b

dataset[dataset["CreditScore"]<l_b]

"""Replace the outliers"""

outlier_list = list(dataset[dataset["CreditScore"] > u_b]["CreditScore"])

outlier_list

outlier_dict = {}.fromkeys(outlier_list,u_b)

outlier_dict

dataset[dataset["CreditScore"]>u_b]

"""Split the data into dependent and independent variables."""

df.head()

x = df.iloc[:,3:13].values  # independant variables

x.shape

y = df.iloc[:,13:14].values # dependant variable

y.shape

"""Check for Categorical columns and perform encoding.

"""

from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer([("oh",OneHotEncoder(),[1,2])],remainder="passthrough")

x = ct.fit_transform(x)

x.shape

df["Geography"].unique()

df["Gender"].unique()

"""Split the data into training and testing"""

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

x_train.shape

x_test.shape