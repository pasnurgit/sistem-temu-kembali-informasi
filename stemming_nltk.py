# Stemming NLTK by PorterStemmer
# Created by : Pasnur
# pasnur@akba.ac.id

# Import library yang dibutuhkan
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 

# Contoh dokumen
dokumen = "I am reading a book. I have some books about information retrieval."

# Menghilangkan tanda baca dan pembuatan token
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(dokumen.lower())

# Menghilangkan stopword
stopword_list =  set(stopwords.words("english"))
token_tanpa_stopword = []
for token in tokens:
    if token not in stopword_list:
        token_tanpa_stopword.append(token)

# Mengubah ke bentuk kata dasar
ps = PorterStemmer()
token_hasil_stemming = []
for token in token_tanpa_stopword:
    token_hasil_stemming.append(ps.stem(token))

# Menampilkan hasil
print("TOKEN SEBELUM STEMMING : ")
print(token_tanpa_stopword)
print("TOKEN SESUDAH STEMMING : ")
print(token_hasil_stemming)