import streamlit as st
from googletrans import Translator
from gtts import gTTS
import tempfile

# App title
st.title("🌍 Language Translator with Voice")

translator = Translator()

# Input text
text = st.text_area("Enter text:")

# Target language selector
lang_map = {
    "te": "Telugu",
    "ta": "Tamil",
    "hi": "Hindi",
    "fr": "French",
    "es": "Spanish",
    "en": "English",
}
target = st.selectbox("Select target language:", list(lang_map.keys()), format_func=lambda x: lang_map[x])

if st.button("Translate & Speak"):
    if text.strip():
        # Translate
        result = translator.translate(text, dest=target)
        st.write(f"🕵️ Detected Language: **{result.src}**")
        st.write(f"✅ Translation ({lang_map[target]}): **{result.text}**")

        # Generate speech
        tts = gTTS(text=result.text, lang=target)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.audio(fp.name, format="audio/mp3")

    else:
        st.warning("Please enter some text to translate.")