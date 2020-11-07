"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

if __name__ == '__main__':
    pass

import argparse
import string
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

parser = argparse.ArgumentParser(description='Toп-100 слов')
parser.add_argument('file', type=str, help='Путь к файлу')
args = parser.parse_args()
print(args.file)
text_file = open(args.file, 'r')
print(text_file.read())
stopwords = set(nltk.corpus.stopwords.words('english'))
tokens = nltk.word_tokenize(text_file)
tokens = [word for word in tokens if (word not in string.punctuation)]
for bad_word in stopwords:
        while bad_word in tokens:
            tokens.remove(bad_word)
word_freq = Counter(tokenized_words)
print(word_freq.most_common(args_values.count))