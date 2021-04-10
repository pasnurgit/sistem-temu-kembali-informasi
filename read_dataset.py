# Membaca Dataset
# Created by : Pasnur
# pasnur@akba.ac.id

# Import library yang dibutuhkan
import os
import xml.etree.ElementTree as et

# Membaca dataset
# Dataset berupa dokumen berita yang disimpan dalam bentuk file XML pada folder dataset
# Setiap data terdiri atas 2 entitas yaitu : <judul> dan <isi>
dataset = os.listdir("dataset")

# Menampilkan isi file dataset
for data in dataset:
    tree = et.parse("dataset/" + data)
    root = tree.getroot()
    judul = root[0][0].text
    isi = root[0][1].text
    print("JUDUL DOKUMEN : " + judul)
    print("ISI DOKUMEN : " + isi)
    print("")