# Pembuatan Inverted Index
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
import pandas as pd

# Membaca dataset
# Dataset berupa dokumen berita yang disimpan dalam bentuk file XML pada folder dataset
# Setiap data terdiri atas 2 entitas yaitu : <judul> dan <isi>
dataset = os.listdir("dataset")
inverted_index = {}
for file_dataset in dataset:
    
    # Melakukan parsing isi file XML
    tree = ET.parse("dataset/" + file_dataset)
    root = tree.getroot()

    # Mengubah semua huruf pada dokumen menjadi huruf kecil
    dokumen_asli = root[0][1].text
    dokumen_hasil_case_folding = dokumen_asli.lower()

    # Menghilangkan tanda baca dan pembuatan token
    tokenizer = RegexpTokenizer(r'\w+')
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
    
    # Melakukan stemming dan membuat daftar term unik
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    token_hasil_stemming = []
    for token in token_tanpa_stopword:
        hasil_stemming = stemmer.stem(token)
        if hasil_stemming in inverted_index:
            if file_dataset in inverted_index[hasil_stemming]:
                inverted_index[hasil_stemming][file_dataset] += 1
            else:
                inverted_index[hasil_stemming][file_dataset] = 1
        else:
            inverted_index[hasil_stemming] = {file_dataset : 1}

# Menampilkan inverted index dalam bentuk DataFrame
jumlah_baris_data = 10
df = pd.DataFrame(inverted_index)
df_transpose = df.transpose()
print(df_transpose.head(jumlah_baris_data))