import streamlit as st
import subprocess

from gnu_files import gnu_py_files, gnu_grc_files, gnu_resource_files, audio_dir, image_dir, file_dir
from gnu_functions import detect_bladeRF, ImageFile, save_file, run_file, generate_st_btns



####################################################################################################################
# Libraries
import streamlit as st
import subprocess
from gnu_files import gnu_py_files, gnu_grc_files, gnu_resource_files, audio_dir
from gnu_functions import detect_bladeRF, save_file, get_st_file_uploader_type, generate_st_btns

# Custom functions
# TODO: add class for audio file
def get_st_audio(audio_path, caption):
    st.markdown(f"### {caption}")
    st.audio(audio_path)
    

type = "audio"
isTransmission_done = False

if type == "audio":
    # type = "an " + type
    (type , file_type, File_Type, folderPath) = (type , "wav", "Audio", audio_dir)
elif type == "image":
    # type = "an " + type
    (type , file_type, File_Type, folderPath) = (type , "png", "Image", image_dir)
elif type == "text":
    # type = "a " + type
    (type , file_type, File_Type, folderPath) = (type , "txt", "Text", file_dir)



####################################################################################################################
# Config
st.set_page_config(f"page_title='CDP - {File_Type} Transfer", page_icon='::', layout='wide')

st.title(f"{File_Type} Transfer")

simulation = st.toggle('Turn on Simulation')

transmission_disabled = True

if not simulation:
    transmission_disabled = False

trainsmitting_status = st.radio(
            "Set the status 👇",
            ["Transmitting", "Receiving"],
            key="transmitting_status",
            disabled=transmission_disabled,
            horizontal=True)

if simulation or (not simulation and trainsmitting_status == "Transmitting"):
    uploaded_file = st.file_uploader(f"Choose {type} file", 
                                 type=file_type,
                                 accept_multiple_files=False)  
    
    if uploaded_file is not None:
        save_file(uploaded_file, folderPath, isInput = True)

        st.success("File is ready.")

# --------------------------------------------------------------------------------------------------------------

# Things to do when simulation is ON
if simulation and uploaded_file is not None:
    st.warning("Simulation is turned on")

    communicate_btn, flowgraph_btn, folder_explorer_btn = generate_st_btns(type=type, folderPath=folderPath, file_status="simulation")
    
    transmitted_file_path = gnu_resource_files[type]["input"]
    received_file_path = gnu_resource_files[type]["output"]

    TransmittedFile = transmitted_file_path
    ReceivedFile = received_file_path

    if communicate_btn:
        # with st.expander("Expand for communication Statistics info"):
        c1, c2, = st.columns(2)
        with c1:
            get_st_audio(TransmittedFile, "Transmitted File")

        with c2:
            get_st_audio(ReceivedFile, "Received File")

        isTransmission_done = True
        
     
# Things to do when you are the transmitter
if (not simulation and trainsmitting_status == "Transmitting") and uploaded_file is not None:
    st.warning("Transmitter : Waiting for realtime transmission")
    
    # Function to check bladeRF status

    # render buttons
    communicate_btn_2, flowgraph_btn_2, folder_explorer_btn_2 = generate_st_btns(type=type, folderPath=folderPath, file_status="real")

    isTransmitDone = True

    st.markdown("___")
    st.markdown("## The transmited file ")

    transmitted_file_path = gnu_resource_files[type]["input"]
    TransmittedFile = transmitted_file_path

    if communicate_btn_2:
        
        get_st_audio(TransmittedFile, "Transmitted Audio")

    st.markdown("___")
    st.markdown("## Import the received file ")
    if isTransmitDone == True:
        uploaded_file = st.file_uploader(f"Choose received {type} file", 
                                 type=file_type,
                                 accept_multiple_files=False)  
    
        if uploaded_file is not None:
            uploaded_file_type = get_st_file_uploader_type(uploaded_file)
            
            if uploaded_file_type == ".wav":
                st.markdown("Received audio")
                st.audio(uploaded_file)
               
            elif uploaded_file_type == ".png":
                st.image(uploaded_file, caption="Received image")

            elif uploaded_file_type == ".txt":
                st.write("Received file")
                file_contents = uploaded_file.read()  # Read the file content
                st.write("### File Contents:")
                st.write(file_contents.decode()) 

            # save_file(uploaded_file, folderPath, isInput = True)
            
            # st.success("File is ready.")


# Things to do when you are the receiver
if (not simulation and trainsmitting_status == "Receiving") :
    st.warning("Receiver : Waiting for realtime receiving")
    

    # Function to check bladeRF status

    # render buttons
    communicate_btn, flowgraph_btn, folder_explorer_btn = generate_st_btns(type=type, folderPath=folderPath, file_status="real",isReceiving=True)

    isTransmitDone = True

    st.markdown("___")
    st.markdown("## The Received file ")

    received_file_path = gnu_resource_files[type]["output"]
    Received_file= received_file_path

    
    if communicate_btn:
        
        if type == "image":
            st.image(Received_file,caption="Received Image")
        elif type == "audio":
            st.write("Received Audio" )
            st.audio(Received_file)
        else:
            raise TypeError(" Only implemented for image and audio")

        # elif type == "fil"

    st.markdown("___")
    st.markdown("## Import the transmitted file ")
    if isTransmitDone == True:
        uploaded_file = st.file_uploader(f"Choose transmitted {type} file", 
                                 type=file_type,
                                 accept_multiple_files=False)  
    
        if uploaded_file is not None:
            uploaded_file_type = get_st_file_uploader_type(uploaded_file)
            
            if uploaded_file_type == ".wav":
                st.write("Transmitted audio")
                st.audio(uploaded_file)
               
            elif uploaded_file_type == ".png":
                st.image(uploaded_file, caption="Transmitted image")

                
            elif uploaded_file_type == ".txt":
                st.write("Transmitted file")
                file_contents = uploaded_file.read()  # Read the file content
                st.write("### File Contents:")
                st.write(file_contents.decode()) 
