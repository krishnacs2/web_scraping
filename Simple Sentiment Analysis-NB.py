from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import nltk
#nltk.download('movie_reviews')
#nltk.download('punkt')

text          = str(input("Enter the text you want you find sentiment for:"))

sent          = TextBlob(text)
# The polarity score is a float within the range [-1.0, 1.0]
# where negative value indicates negative text and positive
# value indicates that the given text is positive.
polarity      = sent.sentiment.polarity
# The subjectivity is a float within the range [0.0, 1.0] where
# 0.0 is very objective and 1.0 is very subjective.
subjectivity  = sent.sentiment.subjectivity

sent          = TextBlob(text, analyzer = NaiveBayesAnalyzer())
classification= sent.sentiment.classification
positive      = sent.sentiment.p_pos
negative      = sent.sentiment.p_neg


print("Polarity:",polarity)

print("Subjectivity:",subjectivity)

print("Classification:",classification)

print("Positive score:",positive*100)

print("Negative score:",negative*100)

