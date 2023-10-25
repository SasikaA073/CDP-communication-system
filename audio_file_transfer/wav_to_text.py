import base64 

file = "sample_wave"

# Open the WAV file in binary mode
with open(f"{file}.wav", 'rb') as wav_file:
    # Read the binary data
    wav_binary_data = wav_file.read()

# Convert the binary data to bytes
bytes_data = bytes(wav_binary_data)

# Encode the bytes as base64
base64_data = base64.b64encode(bytes_data)

# Write the base64 data to a text file
with open('message.txt', 'w') as text_file:
    text_file.write(base64_data.decode('utf-8'))
