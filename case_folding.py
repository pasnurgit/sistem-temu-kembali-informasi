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