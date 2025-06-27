import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Hello Streamlit")

st.write("Hello World")

st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a text")
st.markdown("This is **markdown**")

if st.checkbox("Show/Hide"):
    st.text("Showing or hiding")

if st.button("Click me"):
    st.text("Button clicked")

status = st.radio("Select a status", ("Active", "Inactive"))
st.write(f"Selected status: {status}")

occupation = st.selectbox("Select your occupation", ["Programmer", "Data Scientist", "IT Pro"])
st.write(f"Selected occupation: {occupation}")

locations = st.multiselect("Select your location", ("New York", "London", "Tokyo"))
st.write(f"Selected locations: {locations}")

level = st.slider("Select a level", 1, 10)
st.write(f"Selected level: {level}")

name = st.text_input("Enter your name")
st.write(f"Entered name: {name}")

age = st.number_input("Enter your age")
st.write(f"Entered age: {age}")

bio = st.text_area("Enter your bio")
st.write(f"Entered bio: {bio}")

birth_date = st.date_input("Enter your birth date")
st.write(f"Entered birth date: {birth_date}")

appointment_time = st.time_input("Enter your appointment time")
st.write(f"Entered appointment time: {appointment_time}")

uploaded_file = st.file_uploader("Upload a file")
if uploaded_file is not None:
    st.write("File uploaded successfully")

color = st.color_picker("Pick a color")
st.write(f"Picked color: {color}")

st.header("Dataframe Visualization")

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)

st.header("Graph Examples")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.bar_chart(chart_data)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

st.header("Geospatial Data")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
