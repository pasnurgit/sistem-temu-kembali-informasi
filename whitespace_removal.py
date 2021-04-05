# Import Library
import string

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