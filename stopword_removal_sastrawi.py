# Stopword Removal Sastrawi
# Created by : Pasnur
# pasnur@akba.ac.id

# Import library yang dibutuhkan
from nltk.tokenize import RegexpTokenizer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Contoh dokumen
dokumen = "Saya adalah seorang dosen di kampus STMIK AKBA"

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

# Menampilkan hasil
print("TOKEN ASLI : ")
print(tokens)
print("TOKEN TANPA STOPWORD")
print(token_tanpa_stopword)