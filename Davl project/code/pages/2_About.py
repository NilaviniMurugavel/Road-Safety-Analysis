import streamlit as st
from PIL import Image

st.set_page_config(page_title="About", page_icon="⁉️", layout="wide")
logo = Image.open("D:\College\Sem 4\DAVL\Project\Code\code\logo.jpg")
st.image(logo, width=100)
gif_url = "https://ewscripps.brightspotcdn.com/dims4/default/7c4e68f/2147483647/strip/true/crop/800x450+0+0/resize/320x180!/quality/90/?url=http%3A%2F%2Fewscripps-brightspot.s3.amazonaws.com%2F3d%2F82%2Fcd5de20740f5b50f843fab609997%2Fcaraccidentgif-storyblocks.gif"
st.sidebar.image(gif_url, use_column_width=True)

st.markdown("<h1 style='text-align: center; color:white; font-family: Comic Sans MS;'>ABOUT❕</h1>", unsafe_allow_html=True)
st.write('In todays world road and transport has become an integral partof every human being. Every body is a road user in one shape or the other. The present transport system has minimized the distances but it has on the other hand increased the life risk. Every year road crashes result in loss of lakhs of lives and serious injuries to crores of people.')
st.write('In India itself about eighty thousand people are killed in road crashes every year which is thirteen percent of the total fatality all over the world. Man behind the wheel plays an important role in most of the crashes. In most of the cases crashes occurs either due to carelessness or due to lack of road safety awarenessof the road user. Hence, road safety education is as essential as any other basic skills of survival.')


image_paths = ['https://www.mapsofindia.com/ci-moi-images/my-india/2016/04/road-accidents-in-india.jpg','https://i.ytimg.com/vi/3pKwjbHj1Ms/maxresdefault.jpg','https://assets.telegraphindia.com/telegraph/2021/Nov/1638128124_police.jpg']
image_width=300
image='accident2.jpg'
st.markdown(
    """
    <style>
    .stImage > img {
        display: block;
        margin: 30px auto 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

image_html = ''
for url in image_paths:
    image_html += f'<img src="{url}" style="width:2000px; height:500px; object-fit: cover; display: block;margin-right: 20px;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )



st.sidebar.write("https://morth.nic.in/")
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<h20 style='text-align: right; color:white; font-size: 10px;font-family: Comic Sans MS;'>This app was created as a part of the course project for Data Analysis and Visualization (DAVL).</h20>", unsafe_allow_html=True)
st.markdown("<h25 style='text-align: right; color:white;font-size: 8px; font-family: Comic Sans MS;'>Made with ❤️</h25>", unsafe_allow_html=True)



