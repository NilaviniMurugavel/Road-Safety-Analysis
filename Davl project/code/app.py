import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image

# Define the URL of the "Road Accident" topic page
url = 'https://timesofindia.indiatimes.com/topic/Road-accident?dateFilter=1678645800000,1678732199000'

# Make a GET request to the topic page and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the news items in the HTML content
items = soup.find_all('li', class_='article')

# Extract the news headlines and images from the news items and store them in a list of tuples
data = []
for item in items:
    title = item.find('span', class_='title').text.strip()
    image_url = item.find('img').get('src')
    data.append((title, image_url))

# Display the news headlines and images under the "Latest News" tab

    for title, image_url in data:
        # Load the image from the URL and display it alongside the news headline
        image = Image.open(requests.get(image_url, stream=True).raw)
        st.image(image, width=200)
        st.write(title)
