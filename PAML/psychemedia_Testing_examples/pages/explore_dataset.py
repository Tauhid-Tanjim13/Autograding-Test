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

################################# For checkpoint 2.1 ############################
 # Display feature names and descriptions (from feature_lookup)
def display_features(dataframe):
    counter =0 # Iterate over dataframe features and feature_lookup to show the descriptions and return counter the number of iterations 
    #used over either features or feature lookups....
    for idx, col in enumerate(dataframe.columns):
        counter+=1
        for f in feature_lookup:
            
            if f in dataframe.columns:
                print(col)
                st.markdown('Feature %d - %s'%(idx, feature_lookup[col]))
                break
            else:
                st.markdown('Feature %d - %s'%(idx, col))
                break
    #return len(dataframe.columns)
    return counter
##########################################Checkpoint 2.2 #####################################
def user_input_features():
    numeric_columns = list(df.select_dtypes(['float','int']).columns)
    side_bar_data = {}
    for feature in numeric_columns:
        try:
            f = st.sidebar.slider(str(feature), float(df[str(feature)].min()), float(df[str(feature)].max()), float(df[str(feature)].mean()))
        except Exception as e:
            print(e)
        side_bar_data[feature] = f

    return side_bar_data

def description_selected_features():
    pass

################################################################################# CheckPoint 3 #####

def correlation_selected_features():
    pass


if data:
    st.markdown('### Explore Dataset Features')

    df = read_uploaded_file(data)

    # Restore dataset if already in memory
    st.session_state['house_df'] = df

    # Display feature names and descriptions (from feature_lookup) using display_features helper function
    display_features(df)
    
    # Display dataframe as table
    st.dataframe(df)

     # Select variable to explore  
     ### Select target variable???
    feature_select = st.selectbox(
        label='Select variable to explore',
        options=df.columns
    )

    X = df.loc[:, ~df.columns.isin([feature_select])]
    Y = df.loc[:, df.columns.isin([feature_select])]

    # Visualisation
    st.markdown('### Visualize Features')

    numeric_columns = list(df.select_dtypes(['float','int']).columns)
        # Specify Input Parameters
    st.sidebar.header('Specify Input Parameters')

    st.sidebar.header('Select type of chart')
    chart_select = st.sidebar.selectbox(
        label='Type of chart',
        options=['Scatterplots','Lineplots','Histogram','Boxplot']
    )


