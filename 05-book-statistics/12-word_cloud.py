import os
import collections
from wordcloud import WordCloud


def main():
    filepath = os.path.join('..', 'texts_for_processing', 'Ania z Wyspy, Lucy Maud Montgomery, przełożył Andrzej Magórski.txt')
    with open(filepath, 'r', encoding='utf-8') as book_file:
        book_text = book_file.read()
        words = text_words(book_text)
        word_frequencies = collections.Counter()
        word_frequencies.update(words)
        word_cloud(word_frequencies)


def word_cloud(word_frequencies):
    # Generate a word cloud image
    wordcloud = WordCloud().generate_from_frequencies(word_frequencies)

    # Display the generated image:
    image = wordcloud.to_image()
    image.show()
    image.save('word_cloud.png')


def text_words(text):
    for_removal = ['.', ',', '!', ':', ';', '?', '(', ')', '—', '”', '“']
    for znak in for_removal:
        text = text.replace(znak, " ")
    return text.lower().split()


main()
