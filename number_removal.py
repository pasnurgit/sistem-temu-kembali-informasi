# Number Removal
# Created by : Pasnur
# pasnur@akba.ac.id

# Import library yang dibutuhkan
from nltk.tokenize import RegexpTokenizer

# Contoh dokumen
dokumen = "Kampus STMIK AKBA, berlokasi di Jl. Perintis Kemerdekaan No.75 Makassar"

# Menghilangkan tanda baca dan pembuatan token
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(dokumen.lower())

# Menghilangkan angka
token_tanpa_angka = []
for token in tokens:
    if token.isnumeric() == False:
        token_tanpa_angka.append(token)

# Menampilkan hasil
print(token_tanpa_angka)