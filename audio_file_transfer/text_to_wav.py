import base64

receivedTextFile = "message"
receivedWavFile = receivedTextFile
# Read the base64 data from the text file
with open(f"{receivedTextFile}.txt", 'r') as text_file:
    base64_data = text_file.read()

# Decode the base64 data back to bytes
bytes_data = base64.b64decode(base64_data.encode('utf-8'))

# Write the bytes to a new WAV file
with open(f'{receivedWavFile}.wav', 'wb') as wav_file:
    wav_file.write(bytes_data)
