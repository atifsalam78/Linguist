from googletrans import Translator, LANGUAGES
import pyttsx3
import datetime as d
import speech_recognition as sr



def translate_text(text, target_lang):
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    return translated.text

def print_supported_languages():
    print("Supported languages:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")


if __name__ == "__main__":   
    print("Welcome to the Simple Translator!")
    print_supported_languages()

    source_text = input("Enter the text you want to translate: ")    

    target_lang = input("Enter the language code you want to translate to (e.g., 'es' for Spanish): ")
    if target_lang not in LANGUAGES:
        print("Invalid language code. Please choose from the supported languages.")
    else:
        translated_text = translate_text(source_text, target_lang)
        # translated_text = translated_text.encode("utf-8")    
        print(f"Translated text: {translated_text}")
        
        
