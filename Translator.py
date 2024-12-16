# 5. Write a Python program for a user to enter an English word and output the same in several languages. 
# User can pick any language, just prove that from Google Translator. (10 points)
# prompt: write a python program to translate a word from English from user to multiple languages given by user.
# For example:
# Enter a word to translate: the snow is white
# Enter the languages to translate to (separated by commas): zh-cn,french,vietnamese,spanish,korean
# zh-cn: 雪是白的
# french: la neige est blanche
# vietnamese: tuyết trắng
# spanish: la nieve es blanca
# korean: 눈이 하얗다
# Validate using Google Translate to prove that your python translator is good.

from googletrans import Translator, LANGUAGES

def translate_word():
    translator = Translator()

    while True:
        # Get user input for the phrase to translate
        word = input("Enter a word to translate: ")

        # Get user input for the languages (comma-separated)
        languages_input = input("Enter the languages to translate to (separated by commas): ")
        language_codes = [lang.strip().lower() for lang in languages_input.split(',')]

        # Loop through the specified languages and translate
        for lang in language_codes:
            try:
                # Handle if the user inputs either full language name or code
                if lang in LANGUAGES:
                    dest_language = lang
                else:
                    dest_language = get_lang_code_by_name(lang)

                if dest_language:
                    translation = translator.translate(word, dest=dest_language)
                    print(f"{lang}: {translation.text}")
                else:
                    print(f"Language '{lang}' not found.")

            except Exception as e:
                print(f"Error translating to '{lang}': {e}")

        # Ask the user if they want to continue
        choice = input("\nDo you want to translate another word? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting the translator. Goodbye!")
            break

def get_lang_code_by_name(language_name):
    """Convert a language name to its corresponding language code."""
    for code, name in LANGUAGES.items():
        if language_name in name.lower():
            return code
    return None

# Run the translation function
translate_word()

