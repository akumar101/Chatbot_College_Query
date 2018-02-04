from rake_nltk import Rake
from nltk.stem import PorterStemmer
from num2words import num2words as numConverter

def remove_punctuations(text):
	puncts = '.,!?'
	for symbol in puncts:
		text = text.replace(symbol,' ')
	return text

stemmer = PorterStemmer()
r = Rake()
text = "hello,12 distinguish! distinguishing my name? is avinash and i am bored"
text = remove_punctuations(text)
r.extract_keywords_from_text(text)
data = r.get_ranked_phrases()
data1 = [] 
for i in data:
	temp = i.split(" ")
	for word in temp:
		if(word.isnumeric()):
			word = int(word)
			data1.append(numConverter(word))
		else:
			stemmed_word = stemmer.stem(word.lower())
			if(stemmed_word not in data1):
				data1.append(stemmed_word)
print(data1)
