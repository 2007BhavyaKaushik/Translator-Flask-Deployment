'''
Bhavya kaushik
Bilingual Chatbot

USE: Postman for frontend and testing
'''


from flask import Flask, request, jsonify
from googletrans import Translator
from googletrans.constants import LANGUAGES

app = Flask(__name__)
translator = Translator()
LANGUAGE_CODES = {v.lower(): k for k, v in LANGUAGES.items()}

LANGUAGE_CODES_Extra = {
    'en': 'en',
    'sp': 'es',
    'fr': 'fr',
    'ge': 'de',
    'it': 'it',
    'po': 'pt',
    'ch': 'zh-cn',
    'ja': 'ja',
    'ko': 'ko',
    'ar': 'ar',
    'ru': 'ru',
    'hi': 'hi',
    # Add more languages as needed
}

@app.route('/')
def home():
    return "Welcome to the Translator App!"

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    source_text = data['text']

    if not source_text:
        return jsonify({'error': 'No text provided for translation.'}), 400

    source_lang = get_language_code(data['source_language'])
    target_lang = get_language_code(data['target_lang'])


    if not source_lang or not target_lang:
        return jsonify({'error': 'Invalid or unsupported language code.'}), 400

    try:
        translated = translator.translate(source_text, src=source_lang, dest=target_lang)
        return jsonify({
            'source_language': source_lang,
            'target_language': target_lang,
            'translated_text': translated.text
        })
    except Exception as e:
        return jsonify({'error': f'Error during translation: {str(e)}'}), 500


def get_language_code(language):
    # First try to get the full language code from LANGUAGES
    lang_code = LANGUAGE_CODES.get(language[:2].lower())
    if not lang_code:
        # If not found, fall back to two-letter code from LANGUAGE_CODES_Extra
        lang_code = LANGUAGE_CODES_Extra.get(language[:2].lower())
    return lang_code


if __name__ == '__main__':
    app.run(debug=True)


