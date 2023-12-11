import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from pyvi import ViTokenizer, ViPosTagger
import demoji

def remove_words_not_in_list(text):
    with open('./TuDon.txt', 'r', encoding='utf-8') as file:
        word_list = file.read().splitlines()
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word in word_list]
    return ' '.join(filtered_tokens)


def correct_spelling(text):
    words = ViTokenizer.tokenize(text)
    corrected_words = ViPosTagger.postagging(words)
    corrected_text = ' '.join(corrected_words[0])
    return corrected_text

def remove_emojis(text):
    return demoji.replace_with_desc(text)

