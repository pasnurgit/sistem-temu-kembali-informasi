# Punctuation Removal
# Created by : Pasnur
# pasnur@akba.ac.id

# Import library yang dibutuhkan
import string

# Contoh dokumen
dokumen = "Siapakah, nama Presiden Republik Indonesia? Jawablah dengan tepat!"

# Menghilangkan tanda baca
print(dokumen.translate(str.maketrans("", "", string.punctuation)))