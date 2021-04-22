# Pembobotan TF.IDF
# By Library Scikit-Learn - TfidfVectorizer
# Created by : Pasnur
# pasnur@akba.ac.id

# Import library yang digunakan
import os
import string
import re
import xml.etree.ElementTree as ET
from nltk.tokenize import RegexpTokenizer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Pengaturan pandas
pd.options.display.max_rows = None

# Membaca dataset
# Dataset berupa dokumen berita yang disimpan dalam bentuk file XML pada folder dataset
# Setiap data terdiri atas 2 entitas yaitu : <judul> dan <isi>
dataset = os.listdir("dataset")

# Variabel dokumen untuk menampung hasil text preprocessing dan index
dokumen = []
index = []

# Memproses seluruh dokumen dan term
for file_dataset in dataset:

    # Membuat list index
    index.append(file_dataset[0:4])

    # Melakukan parsing isi file XML
    tree = ET.parse("dataset/" + file_dataset)
    root = tree.getroot()

    # Mengubah semua huruf pada dokumen menjadi huruf kecil
    dokumen_asli = root[0][1].text
    dokumen_hasil_case_folding = dokumen_asli.lower()

    # Menghilangkan tanda baca dan pembuatan token
    tokenizer = RegexpTokenizer(r"\w+")
    tokens = tokenizer.tokenize(dokumen_hasil_case_folding)

    # Menghilangkan angka
    token_tanpa_angka = []
    for token in tokens:
        if token.isnumeric() == False:
            token_tanpa_angka.append(token)

    # Menghilangkan stopword dengan menggunakan library Sastrawi
    factory = StopWordRemoverFactory()
    stopword_list = factory.get_stop_words()
    token_tanpa_stopword = []
    for token in token_tanpa_angka:
        if token not in stopword_list:
            token_tanpa_stopword.append(token)

    # Melakukan stemming dan memasukkan kembali ke dalam bentuk dokumen
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    token_hasil_stemming = []
    for token in token_tanpa_stopword:
        token_hasil_stemming.append(stemmer.stem(token))
    dokumen.append(" ".join(token_hasil_stemming))

# Menghitung nilai TF.IDF
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(dokumen)
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names, index=index)

# Menampilkan hasil perhitungan TF.IDF
print(df.transpose())