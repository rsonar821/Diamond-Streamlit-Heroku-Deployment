import streamlit as st
import pandas as pd
from pickle import load
import sklearn
import numpy as np

df = pd.read_csv("data/diamonds.csv")

scale = load(open("models/scale.pkl", "rb"))
algorithm = load(open("models/decision_tree_regressor.pkl", "rb"))

cut = st.selectbox('Select the cut of the diamond',
('Fair', 'Good', 'Very Good', 'Ideal', 'Premium'))

if cut == 'Fair':
    cut = 1
elif cut == 'Good':
    cut = 2
elif cut == 'Very Good':
    cut = 3
elif cut == 'Ideal':
    cut = 4
elif cut == 'Premium':
    cut = 5

color = st.selectbox('Select the color of the diamond',
('J', 'I', 'H', 'G', 'F', 'E', 'D'))

if color == 'J':
    color = 1
elif color == 'I':
    color = 2
elif color == 'H':
    color = 3
elif color == 'G':
    color = 4
elif color == 'F':
    color = 5
elif color == 'E':
    color = 6
elif color == 'D':
    color = 7    
    
clarity = st.selectbox('Select the clarity of the diamond',
('I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'))

if clarity == 'I1':
    clarity = 1
elif clarity == 'SI2':
    clarity = 2
elif clarity == 'SI1':
    clarity = 3
elif clarity == 'VS2':
    clarity = 4
elif clarity == 'VS1':
    clarity = 5
elif clarity == 'VVS2':
    clarity = 6
elif clarity == 'VVS1':
    clarity = 7
elif clarity == 'IF':
    clarity = 8

carat = st.slider('Select carat of the Diamond', min_value=0.1, max_value=10.00, value=1.00)
x = st.slider('Select diamond length (x) in mm:', min_value=0.1, max_value=20.0, value=1.0)
y = st.slider('Select diamond length (y) in mm:', min_value=0.1, max_value=60.0, value=1.0)
z = st.slider('Select diamond length (z) in mm:', min_value=0.1, max_value=40.0, value=1.0)
depth = st.slider('Select diamond depth:', min_value=0.1, max_value=100.0, value=1.0)
table = st.slider('Select diamond table:', min_value=0.1, max_value=100.0, value=1.0)

data = np.array([carat, cut, color, clarity, depth, table, x, y, z])
data = data.reshape(1, -1)
data = scale.fit_transform(data)
my_prediction = algorithm.predict(data)
my_prediction = round(float(my_prediction), 2)

if st.button('Predict'):
    st.success(f'The diamond price is {my_prediction}$')