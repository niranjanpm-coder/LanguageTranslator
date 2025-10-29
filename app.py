import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

# App title
st.title("🌍 Language Translator with Voice")

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
        # Translate (auto-detects input language)
        translated = GoogleTranslator(source="auto", target=target).translate(text)
        st.write(f"✅ Translation ({lang_map[target]}): **{translated}**")

        # Generate speech
        try:
            tts = gTTS(text=translated, lang=target)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                st.audio(fp.name, format="audio/mp3")
        except Exception as e:
            st.error(f"Speech generation failed: {e}")
    else:
        st.warning("Please enter some text to translate.")