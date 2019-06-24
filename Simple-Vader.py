import nltk
#nltk.download('vader_lexicon')
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentence = str(input("Enter the text you want find sentiment for :\n"))
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

print('Positive words list:',pos_word_list)        
print('Neutral words list:',neu_word_list)    
print('Negative words list:',neg_word_list) 
score = sid.polarity_scores(sentence)
#print('\nScores:', score)


posit = sid.polarity_scores(sentence)['pos']
negat = sid.polarity_scores(sentence)['neg']
neut = sid.polarity_scores(sentence)['neu']

print('\n')

print('Positive score is',sid.polarity_scores(sentence)['pos']*100,'%')
print('Neutral score is',sid.polarity_scores(sentence)['neu']*100,'%')
print('Negative score',sid.polarity_scores(sentence)['neg']*100,'%')

if posit >= negat and posit >=neut :
	print('Overall Sentiment score: Positive')
elif negat > posit and negat>=neut:
	print('Overall Sentiment score : Negative')
else:
	print('Overall Sentiment score : Neutral')

