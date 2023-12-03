# Libraries
import streamlit as st
from gnu_functions import detect_bladeRF, ImageFile
import os

# main_dir = os.path.dirname(__file__)
# output = os.path.join(main_dir, 'output') 

image_path = "./images/"
image_loss = 0

# Global Variables
theme_plotly = None # None or streamlit

# Config
st.set_page_config(page_title='CDP - Image Transfer', page_icon='::', layout='wide')

def get_image_sidebar(img : ImageFile , img_caption):
    st.image(img.get_image_path() , caption=img_caption, use_column_width=None)
    col1, col2 = st.columns(2)
    col1.metric("Size", img.get_image_size())
    col2.metric("Resolution", img.get_image_resolution())

## ----------------------------------------------------------------------------------------------------------------
# Title
st.title('Image Transfer')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

uploaded_file = st.file_uploader("Choose an audio file", 
                                 type="png",
                                 accept_multiple_files=False)  


if uploaded_file is not None:
    st.image(uploaded_file)
    st.write(os.path.dirname(uploaded_file))

# --------------------------------------------------------------------------------------------------------------
simulation = st.toggle('Turn on Simulation')

# Function call to detect bladeRF
bladeRF_status = detect_bladeRF()

if simulation:
    st.write("Simulation is turned on")

    c1, c2, = st.columns(2)
    transmitted_image_path = image_path + "transmitted.png"    
    received_image_path = image_path + "received.png"

    TransmittedImage = ImageFile(transmitted_image_path)
    ReceivedImage = ImageFile(received_image_path)

    with c1:
        get_image_sidebar(TransmittedImage, "Transmitted Image")

    with c2:
        get_image_sidebar(ReceivedImage, "Received Image")
    
    st.write(f"Loss : {image_loss}")
else:
    if not bladeRF_status:
        st.threat("BladeRF not detected for physical channel")
    if bladeRF_status:
        st.success("BladeRF detected")
        trainsmitting_status = st.radio(
            "Set the status 👇",
            ["Transmitting", "Receivnig"],
            key="transmitting_status",
            disabled=False,
            horizontal=True)
        
    if trainsmitting_status == "Transmitting":
        st.write("You are transmitting")

        start_transmitting_btn = st.button("Start Transmitting", type="primary")
        
        if start_transmitting_btn:
            st.success("Transmission Started")





