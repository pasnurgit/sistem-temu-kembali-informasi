# Pembobotan TF.IDF
# Created by : Pasnur
# pasnur@akba.ac.id

# Import library yang digunakan
import os
import string
import re
import copy
import math
import xml.etree.ElementTree as ET
from nltk.tokenize import RegexpTokenizer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import pandas as pd

# Pengaturan pandas
pd.options.display.max_rows = None

# Membaca dataset
# Dataset berupa dokumen berita yang disimpan dalam bentuk file XML pada folder dataset
# Setiap data terdiri atas 2 entitas yaitu : <judul> dan <isi>
dataset = os.listdir("dataset")
jumlah_dokumen = 0
panjang_dokumen = {}
term_list = []
inverted_index = {}

# Memproses seluruh dokumen dan term
for file_dataset in dataset:
    
    # Mengupdate jumlah dokumen
    jumlah_dokumen += 1

    # Inisialisasi panjang dokumen
    panjang_dokumen[file_dataset] = 0

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
    
    # Melakukan stemming dan membuat daftar term unik
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    token_hasil_stemming = []
    for token in token_tanpa_stopword:
        panjang_dokumen[file_dataset] += 1
        hasil_stemming = stemmer.stem(token)
        if hasil_stemming in inverted_index:
            if file_dataset in inverted_index[hasil_stemming]:
                inverted_index[hasil_stemming][file_dataset] += 1
            else:
                inverted_index[hasil_stemming][file_dataset] = 1
        else:
            inverted_index[hasil_stemming] = {file_dataset : 1}
        if hasil_stemming not in term_list:
            term_list.append(hasil_stemming)

# Menghitung nilai TF, DF, IDF, dan TF.IDF
tf = copy.deepcopy(inverted_index)
tf_idf = copy.deepcopy(inverted_index)
df = {}
idf = {}
for term in inverted_index:
    df[term] = len(inverted_index[term])
    idf[term] = round(math.log10(jumlah_dokumen/df[term]), 3)
    for dokumen in inverted_index[term]:
        tf[term][dokumen] = round(inverted_index[term][dokumen] / panjang_dokumen[dokumen], 3)
        tf_idf[term][dokumen] = round(tf[term][dokumen] * idf[term], 3)

# Menampilkan hasil perhitungan TF.IDF
df_inverted_index = pd.DataFrame(inverted_index)
df_inverted_index = df_inverted_index.rename(index=lambda x: "TF_" + x[0:4]).sort_index()
df_tf = pd.DataFrame(tf)
df_tf = df_tf.rename(index=lambda x: "TFN_" + x[0:4]).sort_index()
df_df = pd.DataFrame(df, index=["DF"])
df_idf = pd.DataFrame(idf, index=["IDF"])
df_tf_idf = pd.DataFrame(tf_idf)
df_tf_idf = df_tf_idf.rename(index=lambda x: "TFIDF_" + x[0:4]).sort_index()
hasil = pd.concat([df_inverted_index, df_tf, df_df, df_idf, df_tf_idf])
print(hasil.transpose().fillna(0))