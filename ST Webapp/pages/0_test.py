import streamlit as st
import subprocess
from gnu_files import gnu_py_files, gnu_grc_files

grc_file_path = gnu_grc_files["file"]["simulation"]
st.success(grc_file_path)

file = gnu_py_files["audio"]["simulation"]

main_dir = "../Bit Stream Transfer"

# Command to open GRC file in GNU Radio Companion
command = f"gnuradio-companion {grc_file_path}"



# Function to execute the Python script
def run_python_script():
    global running_process
    
    # Check if the process is already running
    if running_process is None:
        # Start running the Python script
        # running_process = subprocess.Popen(["python3", file])
        # st.write("Python script is running.")

        running_process = subprocess.Popen(["gnuradio-companion",grc_file_path])
        st.success("GNU radio flowgraph is running.")

        # Launch GNU Radio Companion
        # subprocess.Popen(command, shell=True)
        return True
    else:
        # Terminate the running process
        running_process.terminate()
        running_process = None
        st.write("Python script has been terminated.")
        return False

# Initialize running_process as None
running_process = None

# Initialize the session state
if 'running' not in st.session_state:
    st.session_state.running = False

st.title('Toggle Button & Run/Stop Python Script')

# Toggle button
if st.button('Toggle State'):
    # Toggle the state when the button is clicked
    st.session_state.running = not st.session_state.running
    if st.session_state.running:
        st.write('Python script will start on next click.')
    else:
        st.write('Python script will stop on next click.')

# Button to start/stop the Python script
if st.session_state.running:
    if st.button('Run/Stop Python Script'):
        running = run_python_script()
        if running:
            st.write('Python script is running.')
            st.session_state.running = True
        else:
            st.write('Python script has been terminated.')
            st.session_state.running = False
    else:
        st.write('Python script is running.')
else:
    st.write('Python script is stopped.')


import streamlit as st
import os

# Function to find Python files in a directory and its subdirectories
def find_python_files(path):
    python_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

# Streamlit app

st.title('List Python Files in Directory')

# Input for the directory path
directory_path = main_dir
if st.button('List Python Files'):
    if directory_path:
        st.write(f"Python files in '{directory_path}':")
        python_files = find_python_files(directory_path)
        if python_files:
            for file_path in python_files:
                st.write(file_path)
        else:
            st.write("No Python files found in the specified directory.")
    else:
        st.write("Please enter a directory path.")

