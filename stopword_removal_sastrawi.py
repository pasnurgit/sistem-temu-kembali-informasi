# Import Library
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Membuka File
file_dokumen = open("dataset/d001.txt", "r")

# Membaca File
isi_dokumen = file_dokumen.read()

# Menampilkan Isi File
print("Isi Dokumen : ")
print(isi_dokumen)
print("")

# Case Folding
hasil_case_folding = isi_dokumen.lower()
print("Isi Dokumen Hasil Case Folding : ")
print(hasil_case_folding)
print("")

# Punctuation Removal
hasil_punctuation_removal = hasil_case_folding.translate(str.maketrans("","",string.punctuation))
print("Isi Dokumen Hasil Punctuation Removal : ")
print(hasil_punctuation_removal)
print("")

# Whitespace Removal
hasil_whitespace_removal = hasil_punctuation_removal.strip()
print("Isi Dokumen Hasil Whitespace Removal : ")
print(hasil_whitespace_removal)
print("")

# Tokenizing
tokens = word_tokenize(hasil_whitespace_removal)
print("Hasil Tokenizing : ")
print(tokens)
print("")

# Stopword Removal (Bahasa Indonesia)
stopword_list =  set(stopwords.words("indonesian"))
token_hasil_stopword_removal = []
for token in tokens:
    if token not in stopword_list:
        token_hasil_stopword_removal.append(token)
print("Token Hasil Stopword Removal : ")
print(token_hasil_stopword_removal)
print("")

# Stopword Removal by Sastrawi
factory = StopWordRemoverFactory()
stopword_sastrawi = factory.get_stop_words()
token_hasil_stopword_removal_sastrawi = []
for token in tokens:
    if token not in stopword_sastrawi:
        token_hasil_stopword_removal_sastrawi.append(token)
print("Token Hasil Stopword Removal (Sastrawi) : ")
print(token_hasil_stopword_removal_sastrawi)
print("")