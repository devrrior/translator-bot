from textblob import TextBlob

def translate_text(username, text):

    text_blob = TextBlob(text)

    if text_blob.detect_language() == 'es':
        text_translated = text_blob.translate(to='en')
        final_text = f'@{username} {text_translated}'
        return final_text
        # return text_translated

    elif text_blob.detect_language() == 'en':
        text_translated = text_blob.translate(to='es')
        final_text = f'@{username} {text_translated}'
        return final_text
        # return text_translated


if __name__ == '__main__':
    text = input('write: ')
    translate_text(text)