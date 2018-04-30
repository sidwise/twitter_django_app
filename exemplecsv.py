import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download()
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

import csv
import os
def csv_reader(utf8_data, dialect=csv.excel, **kwargs):
	csvreader = csv.reader(utf8_data, delimiter=',', dialect=dialect, **kwargs)
	for row in csvreader:
		yield [unicode(cell, 'utf-8') for cell in row]
abspath = os.path.abspath('all.csv')
cr = csv_reader(open(abspath))


lemm_tab = ["grin","honest"]

# with open('all.csv') as cr:
# 	readcsv = csv.reader(csvfille, delimiter = (','))
def sentiment_tweet(lemm_tab):
	anew = {}
	descriptions   = []
	l_valence_mean = []
	l_valence_SD   = []
	v5 = []
	v8 = []
	for row in cr:

		description  = row[0]
		vals = {'valence_mean' : float(row[2]),
		'valence_SD':  float(row[3]),
		'arousel_mean' : float(row[4]),
		'arousel_SD'  : float(row[5])}
		anew.update({description: vals})

		# descriptions.append(description)
	#print(descriptions)
	print anew
	v1 = 0
	v2=  0
	v3 = 0
	v4 = 0
	sentiment = []
	for term in lemm_tab:
		if anew[term]:
			v1 += anew[term]['valence_mean']/anew[term]['valence_SD']
			v2 += 1/anew[term]['valence_SD']
			v3 += anew[term]['arousel_mean']/anew[term]['arousel_SD']
			v4 += 1/anew[term]['arousel_SD']
	sentiment.append(v1/v2)
	sentiment.append(v3/v4)
	return sentiment

print(sentiment_tweet(lemm_tab))
	# for j in range(0,len(descriptions)):
	# 	if lemm_tab[i] in descriptions[j]:
	# 		v1 = descriptions.index(descriptions[j])
	# 		v2 = l_valence_mean[v1]
	# 		v3 = l_valence_SD[v1]
	# 		v4 = v2 / v3
	# 		v5.append(v4) 
	# 		v6 = sum(v5)
	# 		for k in range(0,len(l_valence_SD)):
	# 			v7 = 1 / l_valence_SD[k]
	# 			v8.append(v7)
	# 			v9 = sum(v8)
	# 			moyemontionnelle = v6 / v9





















