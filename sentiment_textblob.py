from textblob import TextBlob

def analyze_textblob(text):
    score = TextBlob(text).sentiment.polarity
    return score