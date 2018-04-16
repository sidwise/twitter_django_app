import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
#nltk.download()
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
#from nltk.stem import PosterStemmer

twitter = " In the old days, ants and cicadas were friends."

stop_words = set(stopwords.words("english"))
tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(twitter)
print(words)

l = []
lemmes = []
for w in words:
	if w not in stop_words:
		l.append(w)
		print(l)
		
 



lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("cars"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("feet"))
print(lemmatizer.lemmatize("people"))
print(lemmatizer.lemmatize("fantasized", "v"))
print(lemmatizer.lemmatize("cicadas"))
print(lemmatizer.lemmatize("friends"))
print(lemmatizer.lemmatize("broken", "v"))

#ps = PosterStemmer()
#print(ps.stem("broken"))

'''stop_words = set(stopwords.words("english"))
filtered_text = []
lemmatizer = WordNetLemmatizer()
dic = {'tweet[id]': 'lemm'} 

for tweet in search:
    tokens = word_tokenize(tweet['text'])
    print(tokens)
    for token in tokens:
        if token not in stop_words:
            filtered_text.append(token)
            print(filtered_text)
            for word in filtered_text:
                lemm = lemmatizer.lemmatize(filtered_text['word'])
                dic.append(lemm)
                print(dic) '''