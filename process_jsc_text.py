from bs4 import BeautifulSoup


def html2text(doc):
    print('processing {}'.format(doc))
    text = open(doc).read()
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()


def write_file(f, text):
    print('writing {}'.format(f))
    with open(f, mode='w') as file_writer:
        file_writer.write(text)


file1 = 'tashkeela_corpus/aljazeera/aljazeera.txt'
file2 = 'tashkeela_corpus/aljazeera/aljazeera-2016-12-29.b.txt'

doc1 = html2text(file1)
doc2 = html2text(file2)

out1 = 'tashkeela_corpus/aljazeera_processed/aljazeera.txt'
out2 = 'tashkeela_corpus/aljazeera_processed/aljazeera-2016-12-29.b.txt'

write_file(out1, doc1)
write_file(out2, doc2)
