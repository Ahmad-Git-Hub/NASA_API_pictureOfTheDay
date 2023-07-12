import streamlit as st
import requests

api_key = "w8XW6OFXySClhC4kgUGCuoq1quurcJnRpxkhj0i4"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

response1 = requests.get(url)
data = response1.json()

image_filepath = "space_img.png"

response2 = requests.get(data["url"])

with open(image_filepath, "wb") as file:
    file.write(response2.content)


st.header(data["title"])
st.subheader(data["date"])
st.image(image_filepath)
st.write(data["explanation"])
