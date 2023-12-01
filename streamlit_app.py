import streamlit

streamlit.title('My Parents new Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥤 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚🍳 Hard-Boiled Free-Range Eggs')

streamlit.header('Make your own Smoothie')

import pandas as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
