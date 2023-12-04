from PIL import Image
import os
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.io import wavfile
import streamlit as st
import subprocess
from gnu_files import gnu_py_files, gnu_grc_files, gnu_resource_files, audio_dir, image_dir, file_dir


def detect_bladeRF():
    pass
    return True

# Image file class
class ImageFile:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.mode = None
        if self.image is not None:
            self.mode = self.image.mode

        if self.mode == "L":
            self.mode = "Grayscale"
        

    def get_image_resolution_str(self):
        width, height = self.image.size
        return f"{width}x{height} px"
    
    def get_image_file_size(self):
        return str(int(os.stat(self.image_path).st_size // 1000)) + " KB"
    
    def get_image_path(self):
        return self.image_path
    
    def get_image_mode(self):
        return self.mode

    def get_image_resolution(self):
        return self.image.size

    # Check if the mode indicates grayscale or RGB
    def calculate_img_loss(self, rec_img):
        # total_loss = None
        trans_img_mode = self.mode
        rec_img_mode = rec_img.mode

        trans_width, trans_height = self.get_image_resolution()
        rec_width, rec_height = rec_img.get_image_resolution()

        # Check if the size of the images are equal
        if (trans_width, trans_height) != (rec_width, rec_height):
            st.warning("\t- Images resolution mismatched. Please check the images.")

        else: 
            if trans_img_mode == "RGB":
                # Split the image into its red, green, and blue channels
                r_trans, g_trans, b_trans = transmitted_image.split()
                r_rec, g_rec, b_rec = received_image.split()

                # Convet image channels to numpy arrays
                r_trans_pix, g_trans_pix, b_trans_pix = np.array(r_trans), np.array(g_trans), np.array(b_trans)
                r_rec_pix, g_rec_pix, b_rec_pix = np.array(r_rec), np.array(g_rec), np.array(b_rec)

                r_diff = r_trans_pix - r_rec_pix
                g_diff = g_trans_pix - g_rec_pix
                b_diff = b_trans_pix - b_rec_pix

                r_loss = np.sum(r_diff ** 2)
                g_loss = np.sum(g_diff ** 2)
                b_loss = np.sum(b_diff ** 2)

                total_loss = r_loss + g_loss + b_loss


            elif trans_img_mode == "L":
                grayscale_trans_pix = np.array(transmitted_image)
                grayscale_rec_pix = np.array(received_image)

                total_loss = np.sum((grayscale_trans_pix - grayscale_rec_pix) ** 2)

        return total_loss
    


def plot_wav_time_domain(file_path):
    try:
        # Load the WAV file
        sample_rate, data = wavfile.read(file_path)

        # Calculate the duration of the audio in seconds
        duration = len(data) / sample_rate

        # Create a time axis for the audio samples
        time = 1.0 * len(data) / sample_rate
        time_axis = 1.0 * time * (1.0 * range(len(data))) / len(data)

        # Plot the time domain representation
        plt.figure(figsize=(10, 4))
        plt.plot(time_axis, data, color='b')
        plt.title('Time Domain Representation of WAV File')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.show()
    except Exception as e:
        print("An error occurred:", str(e))
    

# function to return the extension of the st.file_uploader
def get_st_file_uploader_type(file: st.file_uploader):
    f_type = file.type 
    f_extension = ""

    # check for file type
    if f_type == "image/png":
        f_extension = ".png"
    elif f_type == "audio/wav":
        f_extension = ".wav"
    elif f_type == "text/plain":
        f_extension = ".txt"
    else:
        raise TypeError("Invalid file type...")

    return f_extension
        
# Function to save uploaded files in a given path 
def save_file(file: st.file_uploader, save_path:str, isInput:bool):
    """"
    Don't add the output file name for save_path.
    """
    f_name = file.name
    f_type = file.type

    # check for file type
    f_out_extension = get_st_file_uploader_type(file)
    f_out_name = ""    
    
    if isInput == True:
        f_out_name = "input"
    if isInput == False:
        f_out_name = "output"

    save_path = save_path + f_out_name + f_out_extension

    # write file to the destination
    with open(save_path, "wb") as f_out:
            f_out.write(file.getvalue())
    
# Function to run file : grc, py, explorer
def run_file(file_path:str, file_type:str):
    if file_type == "py":
        command = "python3"
    elif file_type == "grc":
        command = "gnuradio-companion"
    elif file_type == "folder":
        command = "open"
    else:
        raise TypeError("Not a relevant type : can only open directory, and py,grc files")

    return subprocess.Popen([command, file_path])

# TODO: ALIGN BTNS HORIZONTALLY & ADD FEEDBACK FOR FUNCTION CALLS 
# function to render st buttons 
def generate_st_btns(type="audio",folderPath=audio_dir, file_status = "simulation",isReceiving=False):
    
    communicate_btn_label = None

    if file_status == "simulation":
        communicate_btn_label = "Communicating"
    if (file_status != "simulation") and (isReceiving == True):
        communicate_btn_label = "Receiving"
    if (file_status != "simulation") and (isReceiving == False):
        communicate_btn_label = "Transmitting"

    communicate_btn = st.button(f"Start {communicate_btn_label}")
    flowgraph_btn = st.button("Open flowgraph")
    folder_explorer_btn = st.button("Open directory")

    if communicate_btn:
        run_file(gnu_py_files[type][file_status], file_type="py")

    if flowgraph_btn:
        # st.write(gnu_grc_files[type]["simulation"])
        run_file(gnu_grc_files[type][file_status], file_type="grc")

    if folder_explorer_btn:
        run_file(folderPath , file_type="folder")

    return communicate_btn, flowgraph_btn, folder_explorer_btn


