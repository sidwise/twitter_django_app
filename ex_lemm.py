import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

twitter = [" In the old days, ants and cicadas were friends.",
		   " In the summer, the ant families were very busy.",
		   " While the ants worked hard, the cicadas didn't do anything."
]
	
	


stop_words = set(stopwords.words("english"))
filtered_text = []
lemmatizer = WordNetLemmatizer()
#dic = {'tweet[id]': 'lemm'} 
lemmes = []

for tweet in range(0,len(twitter)):
    tokens = word_tokenize(twitter[tweet])
    print("the tokens are: ", tokens)
    for token in tokens:
    	if token not in stop_words:
            filtered_text.append(token)
            print("the filtrede_text is:", filtered_text)
            for word in range(0,len(filtered_text)):
                lemm = lemmatizer.lemmatize(filtered_text[word])
                lemmes.append(lemm)
                print("the lemmes are:",lemmes)
            