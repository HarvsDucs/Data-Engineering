import streamlit as st
from openai import OpenAI
import tempfile

client = OpenAI(api_key="Your API Key")

uploaded_file = st.file_uploader("Upload an audio file", type=['flac', 'm4a', 'mp3', 'mp4', 'mpeg', 'mpga', 'oga', 'ogg', 'wav', 'webm'])

if uploaded_file is not None:
    # Create a temporary file with the correct extension
    with tempfile.NamedTemporaryFile(delete=False, suffix="." + uploaded_file.name.split('.')[-1]) as tmpfile:
        # Write the uploaded file's bytes to the temporary file
        tmpfile.write(uploaded_file.getvalue())
        tmpfile.flush()  # Ensure all data is written
        
        # Now, pass the temporary file's path to the API
        transcript = client.audio.transcriptions.create(
          model="whisper-1", 
          file=open(tmpfile.name, 'rb')
        )
        
        st.write(transcript)
