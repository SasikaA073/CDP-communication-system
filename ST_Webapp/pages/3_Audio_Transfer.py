# Libraries
import streamlit as st
from gnu_functions import detect_bladeRF, ImageFile, plot_audio_waveform
import subprocess



image_path = "./images/"
image_loss = 0

# Global Variables
theme_plotly = None # None or streamlit

# Config
st.set_page_config(page_title='CDP - Image Transfer', page_icon='::', layout='wide')

# Function to show audio side by side
def get_image_sidebar(img : ImageFile , img_caption):
    st.image(img.get_image_path() , caption=img_caption, use_column_width=None)
    col1, col2 = st.columns(2)
    col1.metric("Size", img.get_image_size())
    col2.metric("Resolution", img.get_image_resolution())


## ----------------------------------------------------------------------------------------------------------

# Title
st.title('Image Transfer')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Upload file
uploaded_file = st.file_uploader("Choose an audio file", 
                                 type="wav",
                                 accept_multiple_files=False)   



# if uploaded_file is not None:
#         st.write(uploaded_file)
#         st.write(type(uploaded_file))
#         st.subheader('Uploaded WAV file')
#         st.audio(uploaded_file)
        

#         with st.expander("Expand for plots"):


#             st.subheader('Waveform Plot')
#             waveform_fig = plot_audio_waveform(uploaded_file)
#             st.plotly_chart(waveform_fig)
running_process = False

def run_python_script():
    global running_process
    
    # Check if the process is already running
    if running_process == False:
        # Start running the Python script
        running_process = subprocess.Popen(["python3", "drawing.py"])
        st.write("Python script is running.")
    else:
        # Terminate the running process
        running_process.terminate()
        running_process != running_process
        st.write("Python script has been terminated.")

if st.button("Run python file"):
    run_python_script()


