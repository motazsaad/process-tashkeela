from bs4 import BeautifulSoup
import re
import string

def html2text(doc):
    print('processing {}'.format(doc))
    html_doc = open(doc).read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    text = soup.get_text()
    return text


def clean_text(doc):
    text = re.sub(r'^https?:\/\/.*[\r\n]*', '', doc, flags=re.MULTILINE)
    text = text.replace('/', ' ')
    text = remove_punctuation(text)
    text = remove_empty_lines(text)
    return text


def remove_punctuation(s):
    my_punctuations = string.punctuation + "،" + "؛" + "؟" + "«" + "»" + 'ـ'
    translator = str.maketrans('', '', my_punctuations)
    return s.translate(translator)


def remove_empty_lines(text):
    lines = [s.rstrip() for s in text.split("\n") if s.rstrip()]
    return '\n'.join(lines)


def write_file(f, text):
    print('writing {}'.format(f))
    with open(f, mode='w') as file_writer:
        file_writer.write(text)


file1 = 'tashkeela_corpus/aljazeera/aljazeera.txt'
file2 = 'tashkeela_corpus/aljazeera/aljazeera-2016-12-29.b.txt'

doc1 = html2text(file1)
doc2 = html2text(file2)

doc1 = clean_text(doc1)
doc2 = clean_text(doc2)

doc = doc1 + '\n\n-------------------\n\n' + doc2
out = 'tashkeela_corpus/aljazeera_processed/jsc.txt'

write_file(out, doc)
