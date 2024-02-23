import streamlit as st
from vscraper import vscraper as vis

st.markdown("<h1 style='text-align: center; font-style: bold;'>Vision Scraper</h1>", unsafe_allow_html=True)
st.write("Please provide the URL from where you would like to scrape the data.")
user_input = st.text_input("URL", "https://www.example.com/")

if st.button('Submit'):
    with st.spinner('Taking Actions!!!'):
        scraper = vis()
        st.write('Instantiating vision scraper...')
        
        screenshot_path = scraper.take_screenshot(user_input)
        st.write('Screenshot taken. Processing the image...')
        
        encoded_image = scraper.encode_image(screenshot_path)
        
        st.write('Fetching response from the scraper...')
        response = scraper.process_image_with_openai(encoded_image)
        
        # Here's where we handle the response
        if response:
            result_content = response.json()['choices'][0]['message']['content']
            st.success('Scraping complete.')
            st.write(result_content)  
        else:
            st.error('No response was received from the scraper.')
