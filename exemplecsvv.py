import csv
import os



def csv_reader(utf8_data, dialect=csv.excel, **kwargs):
	csvreader = csv.reader(utf8_data, delimiter=',', dialect=dialect, **kwargs)
	for row in csvreader:
		yield [unicode(cell, 'utf-8') for cell in row]

abspath = os.path.abspath('all.csv')
cr = csv_reader(open(abspath))


lemm_tab = [ "fraud", "fragrance", "foot", "golfer", "flag"]


# with open('all.csv') as cr:
# 	readcsv = csv.reader(csvfille, delimiter = (','))
def sentiment_tweet(lemm_tab):
	anew = {}
	#descriptions   = []
	#l_valence_mean = []
	#l_valence_SD   = []
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
	#print anew
	v1 = 0
	v2=  0
	v3 = 0
	v4 = 0
	#v5 = 0
	#v6 = 0
	sentiment = []
	for term in lemm_tab:
		if anew[term]:
			v1 += anew[term]['valence_mean']/anew[term]['valence_SD']
			v2 += 1/anew[term]['valence_SD']
			v3 += anew[term]['arousel_mean']/anew[term]['arousel_SD']
			v4 += 1/anew[term]['arousel_SD']
			v5 = v1 / v2
			v6 = v3 / v4
	sentiment.append(v5)
	sentiment.append(v6)

	if 1 < v5< 2 :
		print("sad and upset")
		if 1 < v6 < 2:
			print("Bored")
		elif 2 < v6 < 3:
			print("depressed")
		elif 3 < v6 < 4:
			print("unhappy")
		elif 4 < v6 < 5:
			print("sad")
		elif 5 < v6 < 6:
			print("upset")
		elif 6 < v6 < 7:
			print("stressed")
		elif 7 < v6 < 8:
			print("nervous")
		elif 8 < v6 < 9:
			print("tense")
		
	#-------------------------------------------------------------------------------------------
	elif 2 < v5< 3:
		print('unhappy and stressed')
		if 1 < v6 < 2:
			print("Bored")
		elif 2 < v6 < 3:
			print("depressed")
		elif 3 < v6 < 4:
			print("unhappy")
		elif 4 < v6 < 5:
			print("sad")
		elif 5 < v6 < 6:
			print("upset")
		elif 6 < v6 < 7:
			print("stressed")
		elif 7 < v6 < 8:
			print("nervous")
		elif 8 < v6 < 9:
			print("tense")
	#--------------------------------------------------------------------------------------------

	elif 3 < v5 < 4:
		print("depressed and nervous")
		if 1 < v6 < 2:
			print("Bored")
		elif 2 < v6 < 3:
			print("depressed")
		elif 3 < v6 < 4:
			print("unhappy")
		elif 4 < v6 < 5:
			print("sad")
		elif 5 < v6 < 6:
			print("upset")
		elif 6 < v6 < 7:
			print("stressed")
		elif 7 < v6 < 8:
			print("nervous")
		elif 8 < v6 < 9:
			print("tense")
	#--------------------------------------------------------------------------------------------
	elif 4 < v5 < 5:
		print("bored and tense")
		if 1 < v6 < 2:
			print("Bored")
		elif 2 < v6 < 3:
			print("depressed")
		elif 3 < v6 < 4:
			print("unhappy")
		elif 4 < v6 < 5:
			print("sad")
		elif 5 < v6 < 6:
			print("upset")
		elif 6 < v6 < 7:
			print("stressed")
		elif 7 < v6 < 8:
			print("nervous")
		elif 8 < v6 < 9:
			print("tense")
	#--------------------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------------------
	elif 5 < v5 < 6:
		print("calm and alert")
		if 1 < v6 < 2:
			print("calm")
		elif 2 < v6 < 3:
			print("relaxed")
		elif 3 < v6 < 4:
			print("serene")
		elif 4 < v6 < 5:
			print("contented")
		elif 5 < v6 < 6:
			print("happy")
		elif 6 < v6 < 7:
			print("elated")
		elif 7 < v6 < 8:
			print("excited")
		elif 8 < v6 < 9:
			print("alert")
	#--------------------------------------------------------------------------------------------
	elif 6 < v5 < 7:
		print("relaxed and excited")
		if 1 < v6 < 2:
			print("calm")
		elif 2 < v6 < 3:
			print("relaxed")
		elif 3 < v6 < 4:
			print("serene")
		elif 4 < v6 < 5:
			print("contented")
		elif 5 < v6 < 6:
			print("happy")
		elif 6 < v6 < 7:
			print("elated")
		elif 7 < v6 < 8:
			print("excited")
		elif 8 < v6 < 9:
			print("alert")
	#--------------------------------------------------------------------------------------------
	elif 7 < v5 < 8:
		print("serene and elated")
		if 1 < v6 < 2:
			print("calm")
		elif 2 < v6 < 3:
			print("relaxed")
		elif 3 < v6 < 4:
			print("serene")
		elif 4 < v6 < 5:
			print("contented")
		elif 5 < v6 < 6:
			print("happy")
		elif 6 < v6 < 7:
			print("elated")
		elif 7 < v6 < 8:
			print("excited")
		elif 8 < v6 < 9:
			print("alert")
	#--------------------------------------------------------------------------------------------
	elif 8 < v5 < 9:
		print("contented and happy")
		if 1 < v6 < 2:
			print("calm")
		elif 2 < v6 < 3:
			print("relaxed")
		elif 3 < v6 < 4:
			print("serene")
		elif 4 < v6 < 5:
			print("contented")
		elif 5 < v6 < 6:
			print("happy")
		elif 6 < v6 < 7:
			print("elated")
		elif 7 < v6 < 8:
			print("excited")
		elif 8 < v6 < 9:
			print("alert")
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





















