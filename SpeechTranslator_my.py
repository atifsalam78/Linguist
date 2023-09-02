from googletrans import Translator, LANGUAGES
import pyttsx3
import datetime as d
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def translate_text(text, target_lang):
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    return translated.text

def print_supported_languages():
    print("Supported languages:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

def takeinput():
    '''It takes microphone input from the user and return string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)       

    try:
        print("Recongnizing......")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

if __name__ == "__main__":   
    # takeinput()
    print("Welcome to the Simple Translator!")
    print_supported_languages()

    # source_text = input("Enter the text you want to translate: ")
    source_text = takeinput().lower()

    target_lang = input("Enter the language code you want to translate to (e.g., 'es' for Spanish): ")

    if target_lang not in LANGUAGES:
        print("Invalid language code. Please choose from the supported languages.")
    else:
        translated_text = translate_text(source_text, target_lang)
        # translated_text = translated_text.encode("utf-8")
        speak(translated_text)
        print(f"Translated text: {translated_text}")
        
        
