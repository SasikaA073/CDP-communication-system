import os 

def get_input_file_path(file_name:str):
    # Get the directory of the Python file
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the path for input.png in the same directory
    input_file_path = os.path.join(current_directory, file_name)

    return input_file_path

print(get_input_file_path("input.wav"))
print(type(get_input_file_path("input.wav")))