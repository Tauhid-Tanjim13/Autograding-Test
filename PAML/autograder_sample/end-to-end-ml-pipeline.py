import numpy as np                      # pip install numpy
import pandas as pd                     # pip install pandas
import matplotlib.pyplot as plt         # pip install matplotlib
from sklearn import preprocessing, svm  #  pip install -U scikit-learn 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import streamlit as st                  # pip install streamlit
import time


#############################################

st.markdown("# Practical Applications of Machine Learning (PAML)")

#############################################

st.markdown("### Homework 1 - End-to-End ML Pipeline 🎈")

#############################################

st.markdown("Welcome to the Practical Applications in Machine Learning (PAML) Course! You will build a series of end-to-end ML pipelines, working with various data types and formats, and will need to engineer your system to support training, testing, and deploying ML models.")

st.markdown("**Homework 1:** Your task is to predict median house values in Californian districts, given a number of features from these districts.")

st.write("""You will build a web application that helps Machine Learning Practitioners through an end-to-end ML pipeline.
    
    1. Explore and visualize the data to gain insights.
    2. Preprocess and prepare the data for machine learning algorithms.
    3. Select a model and train it. Fine-tune your model.
    4. Test Model.  Evaluate models using standard metrics.
    5. Deploy your application (present your solution). Launch, monitor, and maintain your system.
""")

st.write("""Future homework assignments will engage students in more an in depth implementation and discussion of ethical implications of four applications.
    
    1. Regression for Predicting Housing Prices
    2. Clustering for Document Retrieval
    3. Classification for Product Recommendation
    4. Deep Learning for Image Search
""")

st.markdown("Click **Explore Dataset** to get started.")