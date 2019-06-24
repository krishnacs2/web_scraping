from urllib.request import HTTPError
import urllib.parse as urlparse
from urllib.request import urlopen
import json
import os,sys
#import urlparse
import requests
import ast

from flask import Flask
from flask import request
from flask import make_response

#self training libs
#import httplib
import json
import os
import urllib, base64
from flask import jsonify
from flask_cors import CORS, cross_origin
import nltk
#nltk.download('vader_lexicon')
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
app = Flask(__name__)
CORS(app, support_credentials=True)

### Intent Handling
	
@app.route('/getSentiment', methods=['POST'])
def createIntent():
	try:	
		req = request.get_json(silent=True, force=True)
		sentence = req.get("text")
		#sentence = str(input("Enter the text you want find sentiment for :\n"))
		tokenized_sentence = nltk.word_tokenize(sentence)

		sid = SentimentIntensityAnalyzer()
		pos_word_list=[]
		neu_word_list=[]
		neg_word_list=[]

		for word in tokenized_sentence:
			if (sid.polarity_scores(word)['compound']) >= 0.1:
				pos_word_list.append(word)
			elif (sid.polarity_scores(word)['compound']) <= -0.1:
				neg_word_list.append(word)
			else:
				 neu_word_list.append(word)                

		#print('Positive words list:',pos_word_list)        
		#print('Neutral words list:',neu_word_list)    
		#print('Negative words list:',neg_word_list) 
		score = sid.polarity_scores(sentence)
		#print('\nScores:', score)


		posit = sid.polarity_scores(sentence)['pos']
		negat = sid.polarity_scores(sentence)['neg']
		neut = sid.polarity_scores(sentence)['neu']
		data = {}
		#print('\n')

		print('Positive score is',sid.polarity_scores(sentence)['pos']*100,'%')
		print('Neutral score is',sid.polarity_scores(sentence)['neu']*100,'%')
		print('Negative score',sid.polarity_scores(sentence)['neg']*100,'%')

		if posit >= negat and posit >=neut :
			#print('Overall Sentiment score: Positive')
			data["sentiment"] = "Positive"
			data["score"] = sid.polarity_scores(sentence)['pos']*100
		elif negat > posit and negat>=neut:
			#print('Overall Sentiment score : Negative')
			data["sentiment"] = "Negative"
			data["score"] = sid.polarity_scores(sentence)['neg']*100
		else:
			#print('Overall Sentiment score : Neutral')
			data["sentiment"] = "Neutral"
			data["score"] = sid.polarity_scores(sentence)['neu']*100

		return jsonify(data)
		
	except OSError as e:
		data = {}
		data['status_code'] = "401"
		data['status'] = str(e)
		#print(json.dumps(data))
		return jsonify(data)
		
		
		
if __name__ == '__main__':

    port = int(os.getenv('PORT', 8000))
    print("Starting app on port %d" % port)
    app.run(debug=True, port=port, host='0.0.0.0',threaded=True)		