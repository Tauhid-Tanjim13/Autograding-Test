import streamlit as st                  
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shap
import plotly.express as px
from sklearn.tree import DecisionTreeRegressor
from pandas.plotting import scatter_matrix


#############################################

st.markdown('# Explore Dataset')

#############################################

st.markdown('### Import Dataset')

##############################################
############### For check point1.1 #################################
def file_uploader():
    return st.file_uploader('Upload a Dataset', type=['csv', 'txt'])

###################################################################
data = file_uploader()

feature_lookup = {
    'longitude':'**longitude** - longitudinal coordinate',
    'latitude':'**latitude** - latitudinal coordinate',
    'housing_median_age':'**housing_median_age** - median age of district',
    'total_rooms':'**total_rooms** - total number of rooms per district',
    'total_bedrooms':'**total_bedrooms** - total number of bedrooms per district',
    'population':'**population** - total population of district',
    'households':'**households** - total number of households per district',
    'median_income':'**median_income** - median income',
    'ocean_proximity':'**ocean_proximity** - distance from the ocean',
    'median_house_value':'median_house_value'
}

################################# For checkpoint 1.2 ###################

def read_uploaded_file(uploaded_file):
    return pd.read_csv(uploaded_file)
###############################################################################

if data:
    read_uploaded_file(data)
