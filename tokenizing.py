# Tokenizing
# Created by : Pasnur
# pasnur@akba.ac.id

# Import library yang dibutuhkan
from nltk.tokenize import RegexpTokenizer

# Contoh dokumen
dokumen = "Kampus STMIK AKBA, berlokasi di Jl. Perintis Kemerdekaan No.75 Makassar"

# Menghilangkan tanda baca dan pembuatan token
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(dokumen.lower())

# Menampilkan hasil
print(tokens)