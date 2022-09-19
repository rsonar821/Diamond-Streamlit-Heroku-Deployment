import streamlit as st
from PIL import Image
import pandas as pd
import seaborn as sns

df = pd.read_csv("data/diamonds.csv")

st.header('Dataset Information')
option=st.selectbox('What would you like to see?',
('Feature Information', 'Dataset Head', 'Dataset Tail', 'Dataset Description'))

if option=='Feature Information':
    st.markdown('''
carat: weight of the diamond (Continuous)

cut: quality of the cut (Fair, Good, Very Good, Premium, Ideal) (Categorical)

color: diamond colour, from J (worst) to D (best) (Categorical)

clarity: a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best)) (Categorical)

depth: total depth percentage = z / mean(x, y) = 2 * z / (x + y) (Continuous)

table: width of top of diamond relative to widest point (Continuous)

price: price in US dollars (Continuous)

x: length in mm (Continuous)

y: width in mm (Continuous)

z: depth in mm (Continuous)
''')

if option=='Dataset Head':
    st.dataframe(df.head())

if option=='Dataset Tail':
    st.dataframe(df.tail())

if option=='Dataset Description':
    st.dataframe(df.describe())

st.header('Data Visualisation')
button = st.radio("Which chart would you like to see?",
('Cut','Color','Clarity','Carat'))
if button=='Cut':
    st.set_option('deprecation.showPyplotGlobalUse', False)
    sns.countplot(data=df, x='cut')
    st.pyplot()
elif button=='Color':
    sns.countplot(data=df, x='color')
    st.pyplot()
elif button=='Clarity':
    sns.countplot(data=df, x='clarity')
    st.pyplot()
elif button=='Carat':
    st.bar_chart(data=df, x='carat', y='price')