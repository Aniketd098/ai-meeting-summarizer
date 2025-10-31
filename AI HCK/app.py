
import streamlit as st
import whisper
import openai
import os

openai.api_key = st.secrets["sk-v_97T-HhfUi995bTw0Quxg"]

st.title("🎙️ AI Meeting Summarizer")

uploaded_file = st.file_uploader("Upload your meeting audio (.mp3 or .wav)", type=["mp3", "wav"])

if uploaded_file:
    with open("audio/temp_audio.mp3", "wb") as f:
        f.write(uploaded_file.read())

    st.info("Transcribing audio...")
    model = whisper.load_model("base")
    result = model.transcribe("audio/temp_audio.mp3")
    transcript = result["text"]
    st.subheader("📝 Transcript")
    st.write(transcript)

    st.info("Generating summary...")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful meeting summarizer."},
            {"role": "user", "content": f"Summarize this meeting:\n{transcript}"}
        ]
    )
    summary = response['choices'][0]['message']['content']
    st.subheader("📌 Summary")
    st.write(summary)