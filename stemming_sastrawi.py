# Stemming Sastrawi
# Created by : Pasnur
# pasnur@akba.ac.id

# Import Library
from nltk.tokenize import RegexpTokenizer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Contoh dokumen
dokumen = "Warga berlarian ketakutan menjauhi lokasi kebakaran"

# Menghilangkan tanda baca dan pembuatan token
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(dokumen.lower())

# Menghilangkan stopword
factory = StopWordRemoverFactory()
stopword_sastrawi = factory.get_stop_words()
token_tanpa_stopword = []
for token in tokens:
    if token not in stopword_sastrawi:
        token_tanpa_stopword.append(token)

# Mengubah ke bentuk kata dasar
factory = StemmerFactory()
stemmer = factory.create_stemmer()
token_hasil_stemming = []
for token in token_tanpa_stopword:
    token_hasil_stemming.append(stemmer.stem(token))

# Menampilkan hasil
print("TOKEN SEBELUM STEMMING : ")
print(token_tanpa_stopword)
print("TOKEN SESUDAH STEMMING : ")
print(token_hasil_stemming)