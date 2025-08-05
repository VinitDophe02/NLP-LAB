import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# 🔤 Sample Text Input
sample_text = """
Hello this is a sample text !. Ok !
"""

# ✅ Step 1: Tokenization
tokens = word_tokenize(sample_text)
print("1️⃣ Tokens:")
print(tokens)

# ✅ Step 2: Remove Punctuation
tokens_no_punct = [word for word in tokens if word not in string.punctuation]
print("\n2️⃣ After Punctuation Removal:")
print(tokens_no_punct)

# ✅ Step 3: Remove Stopwords
stop_words = set(stopwords.words('english'))
tokens_no_stopwords = [word for word in tokens_no_punct if word.lower() not in stop_words]
print("\n3️⃣ After Stop Word Removal:")
print(tokens_no_stopwords)

# ✅ Step 4: Stemming
# Using PorterStemmer
porter = PorterStemmer()
porter_stemmed = [porter.stem(word) for word in tokens_no_stopwords]
print("\n4️⃣ Porter Stemmer:")
print(porter_stemmed)

# Using LancasterStemmer (more aggressive)
lancaster = LancasterStemmer()
lancaster_stemmed = [lancaster.stem(word) for word in tokens_no_stopwords]
print("\n4️⃣ Lancaster Stemmer:")
print(lancaster_stemmed)

# Using SnowballStemmer
snowball = SnowballStemmer("english")
snowball_stemmed = [snowball.stem(word) for word in tokens_no_stopwords]
print("\n4️⃣ Snowball Stemmer:")
print(snowball_stemmed)

# ✅ Step 5: Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word.lower()) for word in tokens_no_stopwords]
print("\n5️⃣ Lemmatized Words:")
print(lemmatized_words)
