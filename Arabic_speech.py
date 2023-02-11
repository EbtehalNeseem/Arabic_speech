from googletrans import Translator
from gtts import gTTS
import playsound

# Initialize the Translator object
translator = Translator(service_urls=['translate.google.com'])

# Translate the text
input_text = "Hello, how are you?"
translated_text = translator.translate(input_text, dest='ar').text

# convert into speech
speech = gTTS(text=translated_text, lang='ar', slow=False)
speech.save("hello.mp3")

playsound.playsound("hello.mp3")
