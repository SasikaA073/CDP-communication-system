from PIL import Image
import os
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.io import wavfile


def detect_bladeRF():
    pass
    return True




class ImageFile:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)

    def get_image_resolution(self):
        width, height = self.image.size
        return f"{width}x{height} px"
    
    def get_image_size(self):
        return str(int(os.stat(self.image_path).st_size // 1000)) + " KB"
    
    def get_image_path(self):
        return self.image_path
    

class AudioFile:
    def __init__(self, audio_path):
        self.audio_path = audio_path
# Function to plot the time-domain representation
def plot_audio_waveform(audio_file):
    # Read the audio file
    audio_data, sample_rate = sf.read(audio_file)

    # Calculate the time axis
    duration = len(audio_data) / sample_rate
    time = np.linspace(0, duration, len(audio_data))

    # Create a Plotly figure for the waveform
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=audio_data, mode='lines', name='Waveform'))
    fig.update_layout(
        title='Audio Waveform',
        xaxis_title='Time (s)',
        yaxis_title='Amplitude',
        template='plotly_dark'
    )

    return fig






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

# Example usage:
file_path = 'path/to/your/file.wav'  # Replace this with the path to your WAV file
plot_wav_time_domain(file_path)
