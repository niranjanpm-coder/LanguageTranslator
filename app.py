import streamlit as st
import asyncio
from googletrans import Translator
from gtts import gTTS
import tempfile



st.title("🌍 Language Translator with Voice")

translator = Translator()

text = st.text_area("Enter text:")

lang_map = {
    "en": "English",
    "te": "Telugu",
    "ta": "Tamil",
    "hi": "Hindi",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "it": "Italian",
}

target = st.selectbox(
    "Select target language:",
    options=list(lang_map.keys()),
    format_func=lambda x: lang_map[x],
)


async def translate_async(text, target):
    result = await translator.translate(text, dest=target)
    return result

def translate_text(text, target):
    result = translator.translate(text, dest=target)
    return result


if st.button("Translate & Speak"):
    if text.strip():
        try:
            # Handle both sync and async behavior
            result = translator.translate(text, dest=target)
            if asyncio.iscoroutine(result):
                result = asyncio.run(result)
            

            st.write(f"🕵️ Detected Language: **{result.src}**")
            st.write(f"✅ Translation ({lang_map[target]}): **{result.text}**")

            # Text to Speech
            tts = gTTS(text=result.text, lang=target)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                tts.save(tmp.name)
                st.audio(tmp.name, format="audio/mp3")

        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
            st.info("Check your internet connection — both Google Translate and gTTS require it.")
    else:
        st.warning("Please enter some text to translate.")