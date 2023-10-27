import streamlit as st

# Define the HTML code to display the news
news_html = """
    <h2>Latest News</h2>
    <ul>
        <li>News item 1</li>
        <li>News item 2</li>
        <li>News item 3</li>
    </ul>
"""

# Define the Streamlit app
def main():
    # Create the menu bar
    menu = ['Home', 'News']
    choice = st.sidebar.selectbox('Select an option', menu)

    # Display the news if the "News" option is selected
    if choice == 'News':
        # Clear the page and display the news HTML
        st.write('')
        st.markdown(news_html, unsafe_allow_html=True)
    else:
        # Display the home page
        st.write('Welcome to my app!')

if __name__ == '__main__':
    main()


forecast="forecast.jpg"

st.markdown(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .center img {
        max-width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="center">', unsafe_allow_html=True)
st.image(forecast, width=700)
st.markdown('</div>', unsafe_allow_html=True)



st.subheader("Share on Social Media")
share_url = "https://example.com/statewise-prediction"
twitter_url = f"https://twitter.com/intent/tweet?url={share_url}&text=Check%20out%20these%20road%20safety%20insights%20for%20different%20states%20in%20India%20%F0%9F%9A%A6%20%F0%9F%87%AE%F0%9F%87%B3%20%23roadsafety%20%23India"
linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url={share_url}&summary=Check%20out%20these%20road%20safety%20insights%20for%20different%20states%20in%20India%20%F0%9F%9A%A6%20%F0%9F%87%AE%F0%9F%87%B3%20%23roadsafety%20%23India"
st.write(f"[Share on Twitter]({twitter_url})")
st.write(f"[Share on LinkedIn]({linkedin_url})")